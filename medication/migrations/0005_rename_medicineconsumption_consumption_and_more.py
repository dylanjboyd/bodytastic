# Generated by Django 4.0.3 on 2022-03-05 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medication', '0004_alter_medicineconsumption_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MedicineConsumption',
            new_name='Consumption',
        ),
        migrations.RenameModel(
            old_name='MedicineSchedule',
            new_name='Schedule',
        ),
    ]
