from django import forms

from .models import RusVersion, EngVersion, RuToEng, Category


class AddWordForm(forms.ModelForm):
    eng_version = forms.CharField(max_length=256, widget=forms.TextInput(
        attrs={'class':'eng_version-area'}
    ))
    rus_version = forms.CharField(max_length=256, widget=forms.TextInput(
        attrs={'class':'rus_version-area'}
    ))
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={'class':'checkbox-area'}
        ),
        error_messages={'required': 'Please select at least one category'},
        required=True
    )

    class Meta:
        model = RuToEng
        fields = ['eng_version', 'rus_version', 'category']

    


  


