# Generated by Django 3.1.7 on 2021-03-30 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtms', '0009_auto_20210330_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
    ]