#!/bin/bash

BACKUP_DIR="$HOME/erp-lab-docs/phase1"
DATE=$(date +%Y%m%d-%H%M)

docker exec odoo18_db_1 pg_dump -U odoo odoo18Docker > "$BACKUP_DIR/odoo_backup_$DATE.sql"

echo "Backup created: $BACKUP_DIR/odoo_backup_$DATE.sql"
