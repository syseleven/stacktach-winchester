"""Stream schema.

Revision ID: 44289d1492e6
Revises: 3ab6d7bf80cd
Create Date: 2014-08-07 07:34:14.721111

"""

# revision identifiers, used by Alembic.
revision = '44289d1492e6'
down_revision = '3ab6d7bf80cd'

from alembic import op
import sqlalchemy as sa
from winchester import models


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stream',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_event', models.PreciseTimestamp(), nullable=False),
    sa.Column('last_event', models.PreciseTimestamp(), nullable=False),
    sa.Column('expire_timestamp', models.PreciseTimestamp(), nullable=True),
    sa.Column('fire_timestamp', models.PreciseTimestamp(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('state', sa.Integer(), nullable=False),
    sa.Column('state_serial_no', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_stream_expire_timestamp', 'stream', ['expire_timestamp'], unique=False)
    op.create_index('ix_stream_fire_timestamp', 'stream', ['fire_timestamp'], unique=False)
    op.create_index('ix_stream_name', 'stream', ['name'], unique=False)
    op.create_index('ix_stream_state', 'stream', ['state'], unique=False)
    op.create_table('dist_trait',
    sa.Column('stream_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('dt_string', sa.String(length=255), nullable=True),
    sa.Column('dt_float', sa.Float(), nullable=True),
    sa.Column('dt_int', sa.Integer(), nullable=True),
    sa.Column('dt_datetime', models.PreciseTimestamp(), nullable=True),
    sa.Column('dt_timerange_begin', models.PreciseTimestamp(), nullable=True),
    sa.Column('dt_timerange_end', models.PreciseTimestamp(), nullable=True),
    sa.ForeignKeyConstraint(['stream_id'], ['stream.id'], ),
    sa.PrimaryKeyConstraint('stream_id', 'name')
    )
    op.create_index('ix_dist_trait_dt_datetime', 'dist_trait', ['dt_datetime'], unique=False)
    op.create_index('ix_dist_trait_dt_float', 'dist_trait', ['dt_float'], unique=False)
    op.create_index('ix_dist_trait_dt_int', 'dist_trait', ['dt_int'], unique=False)
    op.create_index('ix_dist_trait_dt_string', 'dist_trait', ['dt_string'], unique=False)
    op.create_index('ix_dist_trait_dt_timerange_begin', 'dist_trait', ['dt_timerange_begin'], unique=False)
    op.create_index('ix_dist_trait_dt_timerange_end', 'dist_trait', ['dt_timerange_end'], unique=False)
    op.create_table('streamevent',
    sa.Column('stream_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['stream_id'], ['stream.id'], ),
    sa.PrimaryKeyConstraint('stream_id', 'event_id')
    )
    op.create_index('ix_event_generated', 'event', ['generated'], unique=False)
    op.create_index('ix_event_message_id', 'event', ['message_id'], unique=False)
    op.create_index('ix_event_type_id', 'event', ['event_type_id'], unique=False)
    op.create_index('ix_trait_t_datetime', 'trait', ['t_datetime'], unique=False)
    op.create_index('ix_trait_t_float', 'trait', ['t_float'], unique=False)
    op.create_index('ix_trait_t_int', 'trait', ['t_int'], unique=False)
    op.create_index('ix_trait_t_string', 'trait', ['t_string'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_trait_t_string', table_name='trait')
    op.drop_index('ix_trait_t_int', table_name='trait')
    op.drop_index('ix_trait_t_float', table_name='trait')
    op.drop_index('ix_trait_t_datetime', table_name='trait')
    op.drop_index('ix_event_type_id', table_name='event')
    op.drop_index('ix_event_message_id', table_name='event')
    op.drop_index('ix_event_generated', table_name='event')
    op.drop_table('streamevent')
    op.drop_index('ix_dist_trait_dt_timerange_end', table_name='dist_trait')
    op.drop_index('ix_dist_trait_dt_timerange_begin', table_name='dist_trait')
    op.drop_index('ix_dist_trait_dt_string', table_name='dist_trait')
    op.drop_index('ix_dist_trait_dt_int', table_name='dist_trait')
    op.drop_index('ix_dist_trait_dt_float', table_name='dist_trait')
    op.drop_index('ix_dist_trait_dt_datetime', table_name='dist_trait')
    op.drop_table('dist_trait')
    op.drop_index('ix_stream_state', table_name='stream')
    op.drop_index('ix_stream_name', table_name='stream')
    op.drop_index('ix_stream_fire_timestamp', table_name='stream')
    op.drop_index('ix_stream_expire_timestamp', table_name='stream')
    op.drop_table('stream')
    ### end Alembic commands ###
