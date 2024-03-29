"""newsletter

Revision ID: ecb902763029
Revises: 2
Create Date: 2022-02-18 21:59:27.611558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3'
down_revision = '2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('newsletter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('added', sa.DateTime(), server_default=sa.text("(DATETIME('now'))"), nullable=False),
    sa.Column('weekly', sa.DateTime(), nullable=True),
    sa.Column('monthly', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('newsletter')
    # ### end Alembic commands ###
