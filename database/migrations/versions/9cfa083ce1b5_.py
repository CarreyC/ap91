"""empty message

Revision ID: 9cfa083ce1b5
Revises: 
Create Date: 2018-11-05 14:23:36.567237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cfa083ce1b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('realname', sa.String(length=30), nullable=True),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('sex', sa.String(length=10), nullable=True),
    sa.Column('facebook', sa.String(length=60), nullable=True),
    sa.Column('lineid', sa.String(length=60), nullable=True),
    sa.Column('registe_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('facebook'),
    sa.UniqueConstraint('lineid'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
