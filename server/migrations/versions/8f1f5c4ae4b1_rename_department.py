"""rename department

Revision ID: 8f1f5c4ae4b1
Revises: e33b9c913d97
Create Date: 2024-10-09 08:01:24.580884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f1f5c4ae4b1'
down_revision = 'e33b9c913d97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###