#!/bin/sh

echo "=== API Entrypoint ==="

cd /app

echo "--- Unit Tests ---"
python -m test

echo "--- API ---"
python -m api
