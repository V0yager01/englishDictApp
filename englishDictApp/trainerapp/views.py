from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.forms import formset_factory

from wordsApp.models import RuToEng

from .form import ConstructForm, TrainerForm


@login_required()
def construct_trainer_page(request):
    if request.method == "GET":
        form = ConstructForm()
        return render(request, 'construct_trainer.html', context={'form': form})

@login_required()
def trainer_page(request):
    TestFormset = formset_factory(TrainerForm, extra=0)
    if request.method == 'GET':
        word_count = int(request.GET.get('word_count', 0))
        q_category = request.GET.getlist('category', None)
        questions = RuToEng.objects.filter(category__in=q_category).order_by('?')[:word_count]
        questions_list = [{'rus_version': rus.ru_word.word, 'id': rus.id} for rus in questions]
        formset = TestFormset(
            initial=questions_list
        )
        context = {'formset':formset}
        return render(request, 'trainer_page.html', context=context)

    if request.method == 'POST':
        answer_list = []
        formset = TestFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                user_answer = form.cleaned_data.get('eng_version')
                rus_version = form.cleaned_data.get('rus_version')
                id = form.cleaned_data.get('id')
                original_answer = RuToEng.objects.filter(id=id).first()
                is_true = RuToEng.objects.filter(ru_word__word=rus_version, eng_word__word=user_answer).exists()
                answer_list.append(
                            {
                            'form': form,
                            'original_answer':original_answer,
                            'answers_status': is_true
                            }
                        )
            


            context = {'answer_list':answer_list}
            return render(request, 'result_page.html', context=context)

