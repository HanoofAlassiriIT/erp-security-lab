# ERP Security & Cloud Operations Lab

## Phase 1 — Linux + Docker Baseline

### Server Information
- Ubuntu EC2 Server
- Dockerized Odoo 18
- PostgreSQL 13
- AWS Free Tier

---

## Storage Status

Filesystem size:
- Total: 6.8G
- Used: 6.2G
- Available: 562M

Notes:
- Limited storage
- No heavy services allowed
- Need regular cleanup

---

## Memory Status

RAM:
- Total: 957MB
- Used: ~766MB

Notes:
- Lightweight operations only
- Avoid additional containers

---

## Docker Containers

Running containers:
- Odoo 18
- PostgreSQL 13

---

## Docker Storage

Docker image size:
- ~2.4GB

Volumes:
- odoo18_odoo-db-data
- odoo18_odoo-web-data

---

## Operational Notes

- Docker cleanup completed
- Journal logs cleaned
- Temp files cleaned
- Backup exists in Dropbox
