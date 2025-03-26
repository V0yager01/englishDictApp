# Generated by Django 5.1 on 2024-09-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordsApp', '0002_category_remove_rutoeng_category_rutoeng_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=256, unique=True, verbose_name='Название слага'),
        ),
    ]
