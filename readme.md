alembic init migrations
alembic revision --autogenerate -m "Database creation"
alembic upgrade head /(revision_id)

