# Generated by Django 4.2.2 on 2023-06-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_restauran_delete_restaurants'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('items', models.JSONField(default=dict)),
            ],
        ),
        migrations.DeleteModel(
            name='Restauran',
        ),
    ]