"""add content column to posts

Revision ID: 1bd040f00406
Revises: 946392e562dd
Create Date: 2022-06-29 12:44:27.832649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bd040f00406'
down_revision = '946392e562dd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column("posts", 'content')
    pass
