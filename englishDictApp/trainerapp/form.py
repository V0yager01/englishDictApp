from django import forms

from wordsApp.models import Category


class ConstructForm(forms.Form):
    word_count = forms.DecimalField()
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
    )


class TrainerForm(forms.Form):
    id = forms.IntegerField(min_value=0)
    eng_version = forms.CharField(max_length=128)
    rus_version = forms.CharField(max_length=128)