"""empty message

Revision ID: 40e8c5cd2d60
Revises: 
Create Date: 2021-03-16 16:50:46.940823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40e8c5cd2d60'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('property_title', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('rooms', sa.Integer(), nullable=True),
    sa.Column('bathrooms', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('propery_type', sa.String(length=1000), nullable=True),
    sa.Column('location', sa.String(length=1000), nullable=True),
    sa.Column('photo_name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bathrooms'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('location'),
    sa.UniqueConstraint('price'),
    sa.UniqueConstraint('property_title'),
    sa.UniqueConstraint('propery_type'),
    sa.UniqueConstraint('rooms')
    )
    op.create_index(op.f('ix_property_photo_name'), 'property', ['photo_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_property_photo_name'), table_name='property')
    op.drop_table('property')
    # ### end Alembic commands ###
