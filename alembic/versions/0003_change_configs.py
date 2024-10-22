"""empty message

Revision ID: 857e30aea903
Revises: 6c7a1e488c97
Create Date: 2024-10-21 20:28:12.799558

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '857e30aea903'
down_revision: Union[str, None] = '6c7a1e488c97'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('channel_config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('guild_id', sa.BigInteger(), nullable=False),
    sa.Column('config_type', sa.String(), nullable=False),
    sa.Column('channel_id', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message_config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('guild_id', sa.BigInteger(), nullable=False),
    sa.Column('config_type', sa.String(), nullable=False),
    sa.Column('message', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role_config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('guild_id', sa.BigInteger(), nullable=False),
    sa.Column('config_type', sa.String(), nullable=False),
    sa.Column('role_id', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role_config')
    op.drop_table('message_config')
    op.drop_table('channel_config')
    # ### end Alembic commands ###