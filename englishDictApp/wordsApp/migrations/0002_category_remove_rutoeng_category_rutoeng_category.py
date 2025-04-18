# Generated by Django 5.1 on 2024-08-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=256, verbose_name='Название категории')),
            ],
        ),
        migrations.RemoveField(
            model_name='rutoeng',
            name='category',
        ),
        migrations.AddField(
            model_name='rutoeng',
            name='category',
            field=models.ManyToManyField(max_length=256, to='wordsApp.category'),
        ),
    ]
