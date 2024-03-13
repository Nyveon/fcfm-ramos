"""Subplanes ramos

Revision ID: e6fe5bf69f14
Revises: fb143e2066df
Create Date: 2024-03-12 23:35:26.752749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6fe5bf69f14'
down_revision = 'fb143e2066df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subplan_ramo',
    sa.Column('subplan_id', sa.Integer(), nullable=False),
    sa.Column('ramo_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ramo_id'], ['ramo.id'], ),
    sa.ForeignKeyConstraint(['subplan_id'], ['subplan.id'], ),
    sa.PrimaryKeyConstraint('subplan_id', 'ramo_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subplan_ramo')
    # ### end Alembic commands ###
