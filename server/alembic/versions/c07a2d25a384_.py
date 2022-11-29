"""empty message

Revision ID: c07a2d25a384
Revises: 
Create Date: 2022-11-29 11:26:46.764656

"""
import os
import json

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c07a2d25a384'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    users = op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    with open(os.path.join(os.path.dirname(__file__), '../data/users.json')) as file:
        users_data = file.read()
    op.bulk_insert(users, json.loads(users_data))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
