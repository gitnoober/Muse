# Generated by Django 4.0.1 on 2022-01-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0002_alter_spotifytoken_refresh_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytoken',
            name='refresh_token',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
