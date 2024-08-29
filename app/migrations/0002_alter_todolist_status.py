# Generated by Django 5.1 on 2024-08-29 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='status',
            field=models.CharField(choices=[('in_progress', 'In progress'), ('completed', 'Completed')], default='in_progress', max_length=50),
        ),
    ]
