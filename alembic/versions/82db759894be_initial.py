"""initial

Revision ID: 82db759894be
Revises: 
Create Date: 2023-09-06 20:22:26.976929

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82db759894be'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Define your initial database schema here
    conn = op.get_bind()
    if not conn.dialect.has_table(conn, 'users'):
     op.create_table(
        'users',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('user_id'),
    )
    if not conn.dialect.has_table(conn, 'tasks'):
     op.create_table(
        'tasks',
        sa.Column('task_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('description', sa.String()),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), server_onupdate=sa.text('CURRENT_TIMESTAMP')),
        sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
        sa.PrimaryKeyConstraint('task_id'),
    )

    op.create_table(
        'time_entries',
        sa.Column('time_entry_id', sa.Integer(), nullable=False),
        sa.Column('task_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('start_time', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('end_time', sa.DateTime()),
        sa.Column('duration_minutes', sa.Integer()),
        sa.ForeignKeyConstraint(['task_id'], ['tasks.task_id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
        sa.PrimaryKeyConstraint('time_entry_id'),
    )

    op.create_table(
        'reports',
        sa.Column('report_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('description', sa.String()),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
        sa.PrimaryKeyConstraint('report_id'),
    )


def downgrade() -> None:
    # Define the downgrade operation to remove tables if necessary
    op.drop_table('reports')
    op.drop_table('time_entries')
    op.drop_table('tasks')
    op.drop_table('users')
