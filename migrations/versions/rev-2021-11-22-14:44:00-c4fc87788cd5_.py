"""empty message

Revision ID: c4fc87788cd5
Revises: d0b8204bb208
Create Date: 2021-11-22 14:44:00.524120

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'c4fc87788cd5'
down_revision = 'd0b8204bb208'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders_tickets', sa.Column('price', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders_tickets', 'price')
    # ### end Alembic commands ###