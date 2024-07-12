""" File: HealthWatch/migrations/versions/e56fd2f56290_add_email_profile_picture_joined_date_.py

"""

"""Add email, profile_picture, joined_date, and bio to User model

Revision ID: e56fd2f56290
Revises: 
Create Date: 2024-07-11 18:45:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e56fd2f56290'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('profile_picture', sa.String(length=250), nullable=True))
        batch_op.add_column(sa.Column('joined_date', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('bio', sa.Text(), nullable=True))


def downgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('email')
        batch_op.drop_column('profile_picture')
        batch_op.drop_column('joined_date')
        batch_op.drop_column('bio')
