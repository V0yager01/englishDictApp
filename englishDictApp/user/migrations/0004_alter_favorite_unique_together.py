# Generated by Django 5.1 on 2024-09-21 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_user_dictionary_favorite'),
        ('wordsApp', '0002_category_remove_rutoeng_category_rutoeng_category'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('word', 'user')},
        ),
    ]
