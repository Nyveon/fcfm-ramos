"""Subplanes nicknames

Revision ID: 04ca06c178cc
Revises: 5020524c435c
Create Date: 2024-03-13 01:30:39.794185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04ca06c178cc'
down_revision = '5020524c435c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('subplan', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nickname', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('subplan', schema=None) as batch_op:
        batch_op.drop_column('nickname')

    # ### end Alembic commands ###