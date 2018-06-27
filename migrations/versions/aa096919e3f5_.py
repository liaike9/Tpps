"""empty message

Revision ID: aa096919e3f5
Revises: cbb118ce2134
Create Date: 2018-06-27 08:56:39.585024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa096919e3f5'
down_revision = 'cbb118ce2134'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinemas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('district', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.Column('hallnum', sa.Integer(), nullable=True),
    sa.Column('servicecharge', sa.Float(), nullable=True),
    sa.Column('astrict', sa.Integer(), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('showname', sa.String(length=100), nullable=True),
    sa.Column('shownameen', sa.String(length=200), nullable=True),
    sa.Column('director', sa.String(length=100), nullable=True),
    sa.Column('leadingRole', sa.String(length=300), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('language', sa.String(length=50), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('screeningmodel', sa.String(length=20), nullable=True),
    sa.Column('openday', sa.DateTime(), nullable=True),
    sa.Column('backgroundpicture', sa.String(length=100), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    op.drop_table('cinemas')
    # ### end Alembic commands ###