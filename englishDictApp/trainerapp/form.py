from django import forms

from wordsApp.models import Category



class ConstructForm(forms.Form):
    word_count = forms.DecimalField()
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
    )


# class TrainerForm(forms.Form):
#     def __init__(self, questions, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for question in questions:
#             self.fields[str(question.id)] = forms.CharField(
#                 label=question.ru_word.word,
#                 required=False
#             )


class TrainerForm(forms.Form):
    id = forms.IntegerField(min_value=0)
    eng_version = forms.CharField(max_length=128)
    rus_version = forms.CharField(max_length=128)