"""add users table

Revision ID: 252fd793992d
Revises: 1bd040f00406
Create Date: 2022-06-29 12:49:28.257144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '252fd793992d'
down_revision = '1bd040f00406'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                     sa.Column('id', sa.Integer(), nullable = False),
                     sa.Column('email', sa.String(), nullable = False),
                     sa.Column('password', sa.String(), nullable = False),
                     sa.Column('created_at', sa.TIMESTAMP(timezone= True), 
                     server_default =  sa.text('now()'), nullable = False),
                     sa.PrimaryKeyConstraint('id'),
                     sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
