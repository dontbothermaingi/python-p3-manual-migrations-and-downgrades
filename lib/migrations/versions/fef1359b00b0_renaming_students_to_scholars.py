"""Renaming students to scholars

Revision ID: fef1359b00b0
Revises: 791279dd0760
Create Date: 2024-03-14 14:53:56.654538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fef1359b00b0'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
