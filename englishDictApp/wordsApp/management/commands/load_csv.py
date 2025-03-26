import csv

from django.core.management.base import BaseCommand

from wordsApp.models import RusVersion, EngVersion, Category, RuToEng

from .tools.add_words import db_words_models

path = {
     'data/food.csv' : 'food',
     'data/human.csv' : 'human'
}


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for file, category in path.items():
            data_list = {}
            categorty = Category.objects.get(name=category)
            with open(
                    file,
                    'r', encoding='utf-8'
                ) as csv_file:
                    data = csv.DictReader(csv_file)
                    for row in data:
                        eng_w, *ru_w = {**row}.values()
                        data_list[eng_w] = [*ru_w]
            for eng, russ in data_list.items():
                try:
                    db_words_models(eng, russ, categorty)
                except Exception as err:
                    self.stdout.write(self.style.ERROR(f'{err}'))
            self.stdout.write(self.style.SUCCESS('Upload Complete!'))