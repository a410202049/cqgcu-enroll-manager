"""add room rule

Revision ID: 6e06b2ccfbdb
Revises: b1453945c696
Create Date: 2018-06-14 14:22:28.623000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e06b2ccfbdb'
down_revision = 'b1453945c696'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('fee_no', table_name='t_tdtc_fees')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('fee_no', 't_tdtc_fees', ['fee_no'], unique=True)
    # ### end Alembic commands ###