# Generated by Django 4.1.7 on 2023-05-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_first_name_user_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_photos/'),
        ),
    ]
