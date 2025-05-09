# Generated by Django 5.2 on 2025-05-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_educationalvideo_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webinar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Name of the webinar', max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('zoom_registration_url', models.URLField(help_text='Zoom registration link')),
                ('scheduled_time', models.DateTimeField(help_text='When the webinar starts')),
                ('is_active', models.BooleanField(default=True, help_text='Is registration open?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-scheduled_time'],
            },
        ),
    ]
