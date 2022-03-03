# Generated by Django 4.0.3 on 2022-03-01 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('measurement_unit', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BodyAreaReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateField()),
                ('weight_in_g', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sensation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BodyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('notes', models.CharField(blank=True, max_length=500)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='body.bodyareareport')),
            ],
        ),
        migrations.CreateModel(
            name='BodyAreaEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('notes', models.CharField(blank=True, max_length=500)),
                ('body_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='body.bodyarea')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='body.bodyareareport')),
                ('sensations', models.ManyToManyField(to='body.sensation')),
            ],
        ),
    ]
