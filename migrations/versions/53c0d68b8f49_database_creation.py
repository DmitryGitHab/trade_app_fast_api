"""Database creation

Revision ID: 53c0d68b8f49
Revises: 
Create Date: 2023-10-31 21:45:41.207262

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '53c0d68b8f49'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('permissions', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('register_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_services_logs_created_date', table_name='services_logs')
    op.drop_table('services_logs')
    op.drop_index('ix_services_created_date', table_name='services')
    op.drop_index('ix_services_status', table_name='services')
    op.drop_table('services')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('services',
    sa.Column('service_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('status_map', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('created_date', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('update_date', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('service_name', name='services_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_services_status', 'services', ['status'], unique=False)
    op.create_index('ix_services_created_date', 'services', ['created_date'], unique=False)
    op.create_table('services_logs',
    sa.Column('log_uuid', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('service_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_date', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('update_date', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['service_name'], ['services.service_name'], name='services_logs_service_name_fkey'),
    sa.PrimaryKeyConstraint('log_uuid', name='services_logs_pkey')
    )
    op.create_index('ix_services_logs_created_date', 'services_logs', ['created_date'], unique=False)
    op.drop_table('users')
    op.drop_table('roles')
    # ### end Alembic commands ###
