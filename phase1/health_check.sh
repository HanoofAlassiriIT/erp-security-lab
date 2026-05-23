#!/bin/bash
echo "=== Disk Usage ==="
df -h

echo "=== Memory Usage ==="
free -h

echo "=== Running Containers ==="
docker ps

echo "=== Docker Storage ==="
docker system df

echo "=== Odoo Logs Last 20 Lines ==="
docker logs odoo18_web_1 --tail 20
