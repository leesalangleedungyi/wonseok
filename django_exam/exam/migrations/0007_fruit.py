# Generated by Django 4.1.1 on 2022-09-23 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_runner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
