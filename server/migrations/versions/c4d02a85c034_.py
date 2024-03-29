"""empty message

Revision ID: c4d02a85c034
Revises: 8d801b778641
Create Date: 2024-02-23 10:26:06.180992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4d02a85c034'
down_revision = '8d801b778641'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('doctor_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_appointments_table_doctor_id_doctors_table'), 'doctors_table', ['doctor_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments_table', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_appointments_table_doctor_id_doctors_table'), type_='foreignkey')
        batch_op.drop_column('doctor_id')

    # ### end Alembic commands ###
