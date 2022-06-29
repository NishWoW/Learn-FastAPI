"""add remaining columns to posts

Revision ID: dd97eff19a0f
Revises: f0da36d4e224
Create Date: 2022-06-29 13:57:41.047404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd97eff19a0f'
down_revision = 'f0da36d4e224'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable = False, server_default = "TRUE"))
    op.add_column('posts', sa.Column('created_at',sa.TIMESTAMP(timezone= True), server_default =  sa.text('now()'), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
