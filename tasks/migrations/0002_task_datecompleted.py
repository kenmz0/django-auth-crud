# Generated by Django 4.2.5 on 2023-09-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='datecompleted',
            field=models.DateTimeField(null=True),
        ),
    ]
