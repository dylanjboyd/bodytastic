# Generated by Django 4.0.3 on 2022-03-10 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medication', '0007_medicine_current_balance_ledgerentry'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='consumption',
            table='consumption',
        ),
        migrations.AlterModelTable(
            name='ledgerentry',
            table='ledgerentry',
        ),
        migrations.AlterModelTable(
            name='medicine',
            table='medicine',
        ),
        migrations.AlterModelTable(
            name='schedule',
            table='schedule',
        ),
    ]
