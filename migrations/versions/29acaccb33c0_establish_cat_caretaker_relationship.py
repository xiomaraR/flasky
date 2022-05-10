"""Establish cat/caretaker relationship

Revision ID: 29acaccb33c0
Revises: 98aa38545ab9
Create Date: 2022-05-10 10:26:29.613027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29acaccb33c0'
down_revision = '98aa38545ab9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cat', sa.Column('caretaker_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'cat', 'caretaker', ['caretaker_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cat', type_='foreignkey')
    op.drop_column('cat', 'caretaker_id')
    # ### end Alembic commands ###
