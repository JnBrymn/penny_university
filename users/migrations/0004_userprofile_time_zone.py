# Generated by Django 3.0.3 on 2020-03-15 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191209_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='time_zone',
            field=models.CharField(max_length=40, null=True),
        ),
    ]