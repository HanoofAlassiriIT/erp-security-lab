# ERP Security Lab — Odoo on AWS

## Project Overview

This project demonstrates the deployment, operation, and security customization of an Odoo ERP environment on AWS EC2 using Docker.

The project covers infrastructure deployment, ERP functional setup, server health checks, backup awareness, Odoo customization, approval workflows, and email notifications.

---

## Project Phases

### Phase 1 — AWS EC2, Docker, and Odoo Deployment

Deployed Odoo 18 with PostgreSQL on an AWS EC2 Ubuntu server using Docker.

Key work:
- Provisioned an AWS EC2 Ubuntu server.
- Installed and configured Docker.
- Deployed Odoo 18 and PostgreSQL containers.
- Exposed Odoo through port 8069.
- Verified Docker containers and server status.

Skills demonstrated:
- AWS EC2
- Linux server operations
- Docker
- PostgreSQL
- Odoo deployment

---

### Phase 2 — Odoo ERP Functional Setup

Configured and tested basic Odoo ERP workflows.

Key work:
- Configured basic company settings.
- Created sample products and customers.
- Tested quotations and sales orders.
- Tested invoice-related workflows.
- Validated basic ERP process flow.

Skills demonstrated:
- ERP functional configuration
- Odoo Sales workflow
- Quotation and invoice testing
- Business process validation

---

### Phase 3 — Backup, Health Checks, and Server Operations

Documented operational checks and backup awareness for the Odoo server.

Key work:
- Checked disk usage and memory usage.
- Reviewed Docker resource usage.
- Documented server baseline information.
- Created backup and restore notes.
- Documented troubleshooting steps.

Skills demonstrated:
- Linux health checks
- Docker system checks
- Backup and restore awareness
- Server documentation

---

### Phase 4 — Odoo ERP Security Customization and Approval Workflow

Enhanced Odoo security and governance using custom modules.

#### Phase 4A — XML UI Security Customization

Module:
- custom_hide_price

Implemented:
- XML view inheritance.
- XPath customization.
- Hiding sensitive pricing-related fields from the Sales Order interface.

Skills demonstrated:
- Odoo XML customization
- XPath
- View inheritance
- ERP UI security

#### Phase 4B — Backend Validation and Approval Workflow

Module:
- sale_security_validation

Implemented:
- Custom Sales Order fields:
  - Requires Manager Review
  - Approval Reason
  - Manager Review Notified
- Python backend validation.
- Discount approval rule.
- Blocking non-manager users from confirming Sales Orders with discounts above 20%.
- Allowing Sales Managers / Administrators to approve high-discount orders.
- Odoo Chatter notifications.

Skills demonstrated:
- Python
- Odoo ORM
- Backend validation
- Role-based business logic
- Approval workflow design

#### Phase 4C — Email Notification Workflow

Implemented:
- SMTP configuration in Odoo.
- Email notification to managers when a Sales Order requires review.
- Direct Sales Order review link in the email.
- Integration between approval workflow and email alerts.

Skills demonstrated:
- SMTP configuration
- Odoo email workflow
- Notification automation
- ERP process automation

---

## Technologies Used

- AWS EC2
- Ubuntu Linux
- Docker
- PostgreSQL
- Odoo 18
- Python
- XML
- Odoo ORM
- SMTP
- GitHub

---

## Business Value

This project improves ERP governance by reducing the risk of unauthorized discounts and limiting exposure of sensitive pricing information.

It demonstrates how technical controls can enforce internal approval policies inside an ERP system.

---

## Repository Structure

`text
phase1/
phase4/
  modules/
    custom_hide_price/
    sale_security_validation/
  docs/
  screenshots/
docs/
  project-phases-summary.md
Security Notes
The following sensitive items are not included intentionally:
SMTP passwords
Gmail App Passwords
EC2 private keys
Production credentials
Odoo configuration secrets
Real customer data
