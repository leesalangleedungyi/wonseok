# Generated by Django 4.1.1 on 2022-09-23 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_person2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('medal', models.CharField(blank=True, choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronze', 'Bronze')], max_length=10)),
            ],
            options={
                'db_table': 'runner',
            },
        ),
    ]
