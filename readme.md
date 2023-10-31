alembic init migrations
alembic revision --autogenerate -m "Database creation"
alembic upgrade revision_id
