# Generated by Django 4.1.5 on 2023-01-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_is_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_vendor',
            field=models.BooleanField(default=True),
        ),
    ]
