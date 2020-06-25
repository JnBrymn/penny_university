# Generated by Django 2.2.13 on 2020-06-25 12:24
import datetime
from django.db import migrations, models


def set_historical(apps, schema_editor):
    # The chats were imported on June 24th, 2020
    FollowUp = apps.get_model('pennychat', 'FollowUp')
    for follow_up in FollowUp.objects.filter(date__lte=datetime.date(2020, 6, 24)):
        follow_up.historical = True
        follow_up.save()


class Migration(migrations.Migration):

    dependencies = [
        ('pennychat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='followup',
            name='historical',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(set_historical),
    ]
