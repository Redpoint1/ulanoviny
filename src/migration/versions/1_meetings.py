"""meetings

Revision ID: ce4577105bc5
Revises: 
Create Date: 2022-02-16 21:42:39.754009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meeting',
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
    op.drop_table('meeting')
    # ### end Alembic commands ###