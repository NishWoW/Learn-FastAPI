"""add foreign-key to posts

Revision ID: f0da36d4e224
Revises: 252fd793992d
Create Date: 2022-06-29 13:02:10.459219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0da36d4e224'
down_revision = '252fd793992d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete= "CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name= 'posts')
    op.drop_column('posts', 'owner_id')
    pass
