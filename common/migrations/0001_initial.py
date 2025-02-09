# Generated by Django 5.0.6 on 2024-05-21 13:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'feedbacks',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='only_medias/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp', 'mp4', 'avi', 'mpeg4', 'mkv'])], verbose_name='File')),
                ('file_type', models.CharField(choices=[('image', 'Image'), ('video', 'Video')], max_length=10, verbose_name='File Type')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media',
            },
        ),
    ]
