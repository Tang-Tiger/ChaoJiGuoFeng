"""empty message

Revision ID: 2ec8f0c43c0d
Revises: 8f3e6bd57a51
Create Date: 2019-07-05 11:29:15.851689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ec8f0c43c0d'
down_revision = '8f3e6bd57a51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('is_remove', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'is_remove')
    # ### end Alembic commands ###
