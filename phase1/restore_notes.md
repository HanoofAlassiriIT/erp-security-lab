# PostgreSQL Restore Notes

## Restore Command Example

`bash
docker exec -i odoo18_db_1 psql -U odoo -d odoo18Docker < backup_file.sql
