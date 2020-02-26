# Generated by Django 2.2.6 on 2020-02-26 03:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pennychat', '0009_pennychatinvitation'),
    ]

    operations = [
        migrations.AddField(
            model_name='pennychat',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pennychat',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pennychatinvitation',
            name='shares',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='role',
            field=models.IntegerField(choices=[(10, 'Organizer'), (20, 'Attendee'), (30, 'Invitee'), (40, 'Invited NonAttendee')], default=30),  # noqa
        ),
        migrations.AlterField(
            model_name='pennychat',
            name='status',
            field=models.IntegerField(choices=[(10, 'Draft'), (20, 'Shared'), (30, 'Completed'), (40, 'Abandoned')], default=10),  # noqa
        ),
    ]