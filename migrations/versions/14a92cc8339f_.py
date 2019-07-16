"""empty message

Revision ID: 14a92cc8339f
Revises: 
Create Date: 2019-07-16 18:07:17.738195

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '14a92cc8339f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unique_id', sa.String(length=8), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('pw_hash', sa.String(length=255), nullable=True),
    sa.Column('api_key', sa.String(length=500), nullable=True),
    sa.Column('refresh_api_key', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('link',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('long_link', sa.String(length=1000), nullable=True),
    sa.Column('hash_id', sa.String(length=10), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('last_used', sa.DateTime(), nullable=True),
    sa.Column('times_used', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_link_user_id'), 'link', ['user_id'], unique=False)
    op.drop_table('User')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('unique_id', mysql.VARCHAR(length=8), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=150), nullable=True),
    sa.Column('pw_hash', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('api_key', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('refresh_api_key', mysql.VARCHAR(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_index(op.f('ix_link_user_id'), table_name='link')
    op.drop_table('link')
    op.drop_table('user')
    # ### end Alembic commands ###
