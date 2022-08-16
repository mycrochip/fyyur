"""empty message

Revision ID: 9d4541bda5b3
Revises: 
Create Date: 2022-08-06 19:26:39.475158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d4541bda5b3'
down_revision = None
branch_labels = None    
depends_on = None


# Upgrades
def upgrade():
    upgrade_venues_cols()
    upgrade_artists_cols()

def upgrade_venues_cols():
    op.add_column('venues', sa.Column('genres', sa.ARRAY(sa.String(120)), nullable=True))
    op.add_column('venues', sa.Column('website_link', sa.String(120), nullable=True))
    op.add_column('venues', sa.Column('looking_for_talent', sa.Boolean(), nullable=True))
    op.add_column('venues', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('venues', sa.Column('date_created', sa.DateTime(), default=sa.func.current_timestamp()))
    op.add_column('venues', sa.Column('date_updated', sa.DateTime(), default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp()))

    op.execute("UPDATE venues SET looking_for_talent = True WHERE looking_for_talent IS NULL;")

    op.alter_column('venues', 'looking_for_talent', default=True)

def upgrade_artists_cols():
    op.drop_column('artists', 'genres')
    op.add_column('artists', sa.Column('genres', sa.ARRAY(sa.String(120)), nullable=True))
    op.add_column('artists', sa.Column('website_link', sa.String(120), nullable=True))
    op.add_column('artists', sa.Column('looking_for_venues', sa.Boolean(), nullable=True))
    op.add_column('artists', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('artists', sa.Column('date_created', sa.DateTime(), default=sa.func.current_timestamp()))
    op.add_column('artists', sa.Column('date_updated', sa.DateTime(), default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp()))

    op.execute("UPDATE artists SET looking_for_venues = True WHERE looking_for_venues IS NULL;")

    op.alter_column('artists', 'looking_for_venues', default=True)


# Downgrades
def downgrade():
    downgrade_venues_cols()
    downgrade_artists_cols()

def downgrade_venues_cols():
    op.drop_column('venues', 'genres')
    op.drop_column('venues', 'website_link')
    op.drop_column('venues', 'looking_for_talent')
    op.drop_column('venues', 'seeking_description')
    op.drop_column('venues', 'date_created')
    op.drop_column('venues', 'date_updated')

def downgrade_artists_cols():
    op.drop_column('artists', 'genres')
    op.drop_column('artists', 'website_link')
    op.drop_column('artists', 'looking_for_talent')
    op.drop_column('artists', 'seeking_description')
    op.drop_column('artists', 'date_created')
    op.drop_column('artists', 'date_updated')
    op.add_column('artists', sa.Column('genres', sa.String(120)))