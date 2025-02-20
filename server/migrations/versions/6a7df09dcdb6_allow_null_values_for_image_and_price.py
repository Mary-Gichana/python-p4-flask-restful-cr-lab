"""Allow NULL values for image and price

Revision ID: 6a7df09dcdb6
Revises: dd6ff5b60328
Create Date: 2025-01-19 19:42:39.364185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a7df09dcdb6'
down_revision = 'dd6ff5b60328'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('price',
               existing_type=sa.DECIMAL(),
               type_=sa.Float(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(),
               type_=sa.DECIMAL(),
               nullable=False)
        batch_op.alter_column('image',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###
