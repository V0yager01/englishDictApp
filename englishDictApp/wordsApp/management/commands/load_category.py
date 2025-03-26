import csv
from django.core.management.base import BaseCommand
from wordsApp.models import Category


PATH = 'data/categories.csv'

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(PATH, 'r', encoding='utf-8') as csv_file:
            data = csv.reader(csv_file)
            for category in data:
                category = category[0]
                try:
                    Category.objects.create(slug=category.replace(' ', ''), name=category)
                except Exception as err:
                    self.stdout.write(self.style.ERROR(f'{err} {category} already created'))
                         
        self.stdout.write(self.style.SUCCESS('Upload Complete!'))
                    