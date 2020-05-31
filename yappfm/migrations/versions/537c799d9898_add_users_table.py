"""add users table

Revision ID: 537c799d9898
Revises: 
Create Date: 2020-05-31 20:10:15.957054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '537c799d9898'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###