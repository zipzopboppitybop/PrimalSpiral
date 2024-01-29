"""empty message

Revision ID: be284fbc95cc
Revises: fb92587bf00e
Create Date: 2024-01-28 18:16:59.528682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be284fbc95cc'
down_revision = 'fb92587bf00e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hashed_password', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('bio', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('bio')
        batch_op.drop_column('hashed_password')

    # ### end Alembic commands ###