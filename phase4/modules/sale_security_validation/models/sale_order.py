from odoo import models, fields, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    requires_manager_review = fields.Boolean(
        string='Requires Manager Review',
        copy=False
    )

    approval_reason = fields.Char(
        string='Approval Reason',
        copy=False
    )

    manager_review_notified = fields.Boolean(
        string='Manager Review Notified',
        copy=False,
        default=False
    )

    def _get_high_discount_lines(self, threshold):
        self.ensure_one()
        return self.order_line.filtered(
            lambda line: getattr(line, 'discount', 0.0) and line.discount > threshold
        )

    def _get_sales_manager_partners(self):
        group = self.env.ref('sales_team.group_sale_manager', raise_if_not_found=False)
        if group:
            return group.users.mapped('partner_id').filtered(lambda p: p.active)

        admin = self.env.ref('base.user_admin', raise_if_not_found=False)
        return admin.partner_id if admin else self.env['res.partner']


    def _send_email_to_partners(self, partners, subject, message):
        self.ensure_one()

        email_partners = partners.filtered(lambda p: p.email)
        if not email_partners:
            return

        email_from = (
            self.env.user.partner_id.email_formatted
            or self.env.company.partner_id.email_formatted
            or 'odoo@example.com'
        )

        for partner in email_partners:
            self.env['mail.mail'].sudo().create({
                'subject': subject,
                'email_from': email_from,
                'email_to': partner.email,
                'body_html': message.replace('\n', '<br/>'),
                'auto_delete': False,
            }).sudo().send(raise_exception=False)

    def _notify_sales_managers(self, threshold, max_discount):
        self.ensure_one()

        partners = self._get_sales_manager_partners()

        message = (
            "Manager Review Required\n\n"
            "Sales Order %s contains a high discount of %.2f%%.\n"
            "Allowed threshold: %.2f%%.\n\n"
            "Please review this order before confirmation."
        ) % (self.name, max_discount, threshold)

        self.message_post(
            body=message,
            subject='Manager Review Required',
            partner_ids=partners.ids,
            message_type='notification',
            subtype_xmlid='mail.mt_comment'
        )

        channel_model = False
        if self.env.registry.get('discuss.channel'):
            channel_model = 'discuss.channel'
        elif self.env.registry.get('mail.channel'):
            channel_model = 'mail.channel'

        if channel_model:
            channel = self.env[channel_model].sudo().search(
                [('name', 'ilike', 'general')],
                limit=1
            )
            if channel:
                channel.message_post(
                    body=message,
                    subject='Manager Review Required',
                    message_type='comment',
                    subtype_xmlid='mail.mt_comment'
                )

    def _post_manager_approval_note(self, threshold, max_discount):
        self.ensure_one()

        message = (
            "Manager Approval Completed\n\n"
            "Sales Manager %s approved Sales Order %s with a high discount of %.2f%%.\n"
            "Allowed threshold: %.2f%%."
        ) % (self.env.user.name, self.name, max_discount, threshold)

        self.message_post(
            body=message,
            subject='High Discount Approved by Manager',
            message_type='comment',
            subtype_xmlid='mail.mt_comment'
        )

        requester = self.create_uid.partner_id
        if requester:
            self._send_email_to_partners(
                requester,
                'High Discount Approved - %s' % self.name,
                message
            )

    def action_confirm(self):
        threshold = 20.0
        is_sales_manager = self.env.user.has_group('sales_team.group_sale_manager')

        for order in self:
            high_discount_lines = order._get_high_discount_lines(threshold)

            if high_discount_lines:
                max_discount = max(high_discount_lines.mapped('discount'))

                if not is_sales_manager:
                    order.write({
                        'requires_manager_review': True,
                        'approval_reason': 'Discount %.2f%% exceeds the allowed threshold of %.2f%%.' % (max_discount, threshold),
                        'manager_review_notified': True,
                    })

                    order._notify_sales_managers(threshold, max_discount)

                    return {
                        'type': 'ir.actions.client','tag': 'display_notification',
                        'params': {
                            'title': _('Manager Review Required'),
                            'message': _('This order contains a high discount and requires manager review before confirmation.'),
                            'type': 'warning',
                            'sticky': True,
                        }
                    }

                order._post_manager_approval_note(threshold, max_discount)
                order.write({
                    'requires_manager_review': False,
                    'approval_reason': 'Approved by Sales Manager %s for %.2f%% discount.' % (self.env.user.name, max_discount),
                    'manager_review_notified': False,
                })

        return super().action_confirm()
