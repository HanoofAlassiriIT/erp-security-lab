# ERP Security Lab — Project Phases Summary

## Project Overview

This project demonstrates the deployment, configuration, operation, and security customization of an Odoo ERP environment on AWS EC2 using Docker.

The project was developed in multiple phases, starting from infrastructure deployment and ending with ERP security customization, approval workflows, and email notifications.

---

## Phase 1 — AWS EC2, Docker, and Odoo Deployment

### Objective
Deploy an Odoo 18 ERP environment on an AWS EC2 Ubuntu server using Docker and PostgreSQL.

### Key Activities
- Provisioned an AWS EC2 Ubuntu server.
- Installed and configured Docker.
- Deployed Odoo 18 and PostgreSQL containers.
- Exposed Odoo through port 8069.
- Verified container status and system resources.
- Created baseline server documentation.

### Skills Demonstrated
- AWS EC2 administration.
- Linux server operations.
- Docker container management.
- PostgreSQL container deployment.
- Basic server troubleshooting.

---

## Phase 2 — Odoo ERP Functional Setup

### Objective
Configure Odoo ERP basics and validate core business workflows.

### Key Activities
- Configured basic Odoo company settings.
- Created sample products and customers.
- Tested Sales workflow using Quotations and Sales Orders.
- Generated invoices and reviewed invoice-related outputs.
- Used Odoo data and reports to validate the ERP workflow.

### Skills Demonstrated
- ERP functional configuration.
- Sales and invoicing workflow testing.
- Odoo business process validation.
- Basic ERP data handling.

---

## Phase 3 — Backup, Health Checks, and Server Operations

### Objective
Improve operational reliability by documenting backup, restore, health check, and troubleshooting procedures.

### Key Activities
- Checked EC2 disk usage, memory, and Docker resource usage.
- Documented server baseline status.
- Created backup and restore notes.
- Reviewed database and Odoo container health.
- Documented common troubleshooting steps.

### Skills Demonstrated
- Linux system monitoring.
- Docker operational checks.
- Backup and restore awareness.
- Server health validation.
- Technical documentation.

---

## Phase 4 — Odoo ERP Security Customization and Approval Workflow

### Objective
Enhance ERP security and governance through UI customization, backend validation, approval workflows, and email notifications.

### Phase 4A — XML UI Security Customization
- Created a custom Odoo module to hide sensitive pricing-related fields.
- Used XML view inheritance and XPath.
- Hid pricing fields from Sales Order views.

### Phase 4B — Backend Validation and Approval Workflow
- Created a custom Python module for Sales Order validation.
- Added custom approval fields.
- Prevented non-manager users from confirming Sales Orders with discounts above 20%.
- Allowed Sales Managers / Administrators to approve high-discount orders.
- Added Odoo Chatter notifications.

### Phase 4C — Email Notification Workflow
- Configured SMTP in Odoo.
- Sent email notifications to managers when review is required.
- Included direct Sales Order links in email notifications.
- Integrated email alerts with the approval workflow.

### Skills Demonstrated
- Odoo XML customization.
- Odoo Python development.
- Odoo ORM.
- Role-based approval logic.
- SMTP email workflow.
- ERP security governance.
- Docker-based Odoo deployment.
