# Generated by Django 4.0.3 on 2022-03-03 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0003_alter_bodyarea_options_alter_sensation_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bodyareaentry',
            options={'ordering': ['body_area']},
        ),
    ]
