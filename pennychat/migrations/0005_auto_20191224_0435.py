# Generated by Django 2.2.6 on 2019-12-24 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pennychat', '0004_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pennychat',
            name='user',
            field=models.TextField(null=True),
        ),
    ]