"""empty message

Revision ID: e627519f4032
Revises: 23f05225dcaf
Create Date: 2022-04-03 03:43:37.083612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e627519f4032'
down_revision = '23f05225dcaf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'is_retail',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_constraint('products_category_id_fkey', 'products', type_='foreignkey')
    op.drop_constraint('products_user_id_fkey', 'products', type_='foreignkey')
    op.create_foreign_key(None, 'products', 'category', ['category_id'], ['category_id'])
    op.create_foreign_key(None, 'products', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.create_foreign_key('products_user_id_fkey', 'products', 'users', ['user_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key('products_category_id_fkey', 'products', 'category', ['category_id'], ['category_id'], ondelete='SET NULL')
    op.alter_column('products', 'is_retail',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###
