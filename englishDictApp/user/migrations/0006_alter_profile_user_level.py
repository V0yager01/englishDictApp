# Generated by Django 5.1 on 2024-11-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_profile_user_dictionary_profile_user_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_level',
            field=models.CharField(choices=[('Fool', 'Fool'), ('Begginer', 'Begginer'), ('Advance', 'Advance'), ('Pro', 'Pro'), ('SuperPro', 'SuperPro')], default='Fool', max_length=128),
        ),
    ]
