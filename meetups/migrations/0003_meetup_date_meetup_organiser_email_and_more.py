# Generated by Django 4.0.3 on 2022-04-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_participant_meetup_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2022-04-08'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='organiser_email',
            field=models.EmailField(default='test@test.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meetup',
            name='participants',
            field=models.ManyToManyField(blank=True, to='meetups.participant'),
        ),
    ]
