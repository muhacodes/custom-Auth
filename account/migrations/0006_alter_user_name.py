# Generated by Django 4.1.7 on 2023-08-28 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_name_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]