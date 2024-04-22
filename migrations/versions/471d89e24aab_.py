"""empty message

Revision ID: 471d89e24aab
Revises: 93a50a8b808a
Create Date: 2024-04-22 15:48:07.700529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '471d89e24aab'
down_revision = '93a50a8b808a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.String(length=120), nullable=False))
        batch_op.create_unique_constraint(None, ['address'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('address')

    # ### end Alembic commands ###
