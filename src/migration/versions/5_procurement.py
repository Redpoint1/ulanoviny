"""procurement

Revision ID: ba528aed10dd
Revises: 4
Create Date: 2022-02-19 00:17:06.955668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5'
down_revision = '4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('procurement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('added', sa.DateTime(), server_default=sa.text("(DATETIME('now'))"), nullable=False),
    sa.Column('weekly', sa.DateTime(), nullable=True),
    sa.Column('monthly', sa.DateTime(), nullable=True),
    sa.Column('is_offer', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('procurement')
    # ### end Alembic commands ###
