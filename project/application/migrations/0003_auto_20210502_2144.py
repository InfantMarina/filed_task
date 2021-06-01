# Generated by Django 3.1.6 on 2021-05-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_song_file_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_book',
            name='uploaded_time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='uploaded_time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='uploaded_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]