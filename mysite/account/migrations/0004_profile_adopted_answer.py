# Generated by Django 4.0.5 on 2022-06-23 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_git_address_alter_profile_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='adopted_answer',
            field=models.PositiveIntegerField(default=0),
        ),
    ]