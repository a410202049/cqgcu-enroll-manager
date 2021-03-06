"""modify order

Revision ID: 70c83b17cc78
Revises: 5bd08103a3de
Create Date: 2018-06-13 10:36:58.569000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70c83b17cc78'
down_revision = '5bd08103a3de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_order', sa.Column('pay_time', sa.DATETIME(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('t_order', 'pay_time')
    # ### end Alembic commands ###
