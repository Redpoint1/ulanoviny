"""contract

Revision ID: 36cfbddb113e
Revises: 8
Create Date: 2022-02-27 04:28:39.467629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9'
down_revision = '8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contract',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('published', sa.Date(), nullable=False),
    sa.Column('added', sa.DateTime(), server_default=sa.text("(DATETIME('now'))"), nullable=False),
    sa.Column('size_in_mb', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('weekly', sa.DateTime(), nullable=True),
    sa.Column('monthly', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contract')
    # ### end Alembic commands ###