"""Adicionado indioma nas postagens

Revision ID: 8d0b601e8973
Revises: f374f598e838
Create Date: 2022-02-04 21:09:34.497879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d0b601e8973'
down_revision = 'f374f598e838'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'language')
    # ### end Alembic commands ###
