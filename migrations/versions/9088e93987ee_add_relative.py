"""add relative

Revision ID: 9088e93987ee
Revises: 73ef6a7390c8
Create Date: 2018-06-14 13:57:50.164000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9088e93987ee'
down_revision = '73ef6a7390c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_tdtc_orders', sa.Column('amt', sa.DECIMAL(precision=12, scale=2), nullable=True))
    op.add_column('t_tdtc_orders', sa.Column('begin_time', sa.DATETIME(), nullable=True))
    op.add_column('t_tdtc_orders', sa.Column('detect_amt', sa.DECIMAL(precision=12, scale=2), nullable=True))
    op.add_column('t_tdtc_orders', sa.Column('fee_desc', sa.String(length=128), nullable=True))
    op.add_column('t_tdtc_orders', sa.Column('fee_no', sa.String(length=32), nullable=True))
    op.add_column('t_tdtc_orders', sa.Column('loan_amt', sa.DECIMAL(precision=12, scale=2), nullable=True))
    op.add_column('t_tdtc_orders', sa.Column('paid_amt', sa.DECIMAL(precision=12, scale=2), nullable=True))
    op.add_column('t_tdtc_orders', sa.Column('refund_amt', sa.DECIMAL(precision=12, scale=2), nullable=True))
    op.add_column('t_tdtc_orders', sa.Column('year', sa.String(length=8), nullable=True))
    op.create_unique_constraint(None, 't_tdtc_orders', ['fee_no'])
    op.drop_column('t_tdtc_orders', 'status')
    op.drop_column('t_tdtc_orders', 'real_pay_amt')
    op.drop_column('t_tdtc_orders', 'pay_time')
    op.drop_column('t_tdtc_orders', 'should_pay_amt')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_tdtc_orders', sa.Column('should_pay_amt', mysql.DECIMAL(precision=12, scale=2), nullable=True))
    op.add_column('t_tdtc_orders', sa.Column('pay_time', mysql.DATETIME(), nullable=True))
    op.add_column('t_tdtc_orders', sa.Column('real_pay_amt', mysql.DECIMAL(precision=12, scale=2), nullable=True))
    op.add_column('t_tdtc_orders', sa.Column('status', mysql.VARCHAR(length=24), nullable=True))
    op.drop_constraint(None, 't_tdtc_orders', type_='unique')
    op.drop_column('t_tdtc_orders', 'year')
    op.drop_column('t_tdtc_orders', 'refund_amt')
    op.drop_column('t_tdtc_orders', 'paid_amt')
    op.drop_column('t_tdtc_orders', 'loan_amt')
    op.drop_column('t_tdtc_orders', 'fee_no')
    op.drop_column('t_tdtc_orders', 'fee_desc')
    op.drop_column('t_tdtc_orders', 'detect_amt')
    op.drop_column('t_tdtc_orders', 'begin_time')
    op.drop_column('t_tdtc_orders', 'amt')
    # ### end Alembic commands ###