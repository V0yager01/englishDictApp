from django.db import transaction

from wordsApp.models import RusVersion, EngVersion, RuToEng

@transaction.atomic
def db_words_models(eng: str, rus: list[str], category):
    eng_model = EngVersion.objects.create(word=eng)
    rus_models = [RusVersion.objects.create(word=word) for word in rus if word]
    rte_model = [RuToEng.objects.create(eng_word=eng_model, ru_word=ru) for ru in rus_models]
    [model.category.add(category) for model in rte_model]
    return rte_model

