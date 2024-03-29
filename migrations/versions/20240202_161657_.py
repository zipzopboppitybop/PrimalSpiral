"""empty message

Revision ID: 753971d6c760
Revises: be284fbc95cc
Create Date: 2024-02-02 16:16:57.736952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '753971d6c760'
down_revision = 'be284fbc95cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('deck_list')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deck_list',
    sa.Column('deckId', sa.INTEGER(), nullable=True),
    sa.Column('cardId', sa.INTEGER(), nullable=True),
    sa.Column('amount', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['cardId'], ['cards.id'], ),
    sa.ForeignKeyConstraint(['deckId'], ['decks.id'], )
    )
    # ### end Alembic commands ###