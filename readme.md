alembic init migrations
alembic revision --autogenerate -m "Database creation"
alembic upgrade head /(revision_id)


celery -A src.tasks.tasks:celery worker --loglevel=INFO --pool=solo 
celery -A src.tasks.tasks:celery flower


