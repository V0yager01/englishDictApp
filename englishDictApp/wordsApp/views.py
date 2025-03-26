from collections import defaultdict

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef

from .form import AddWordForm
from .models import Category, RuToEng, EngVersion, RusVersion


from user.models import Favorite


def index(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'index.html',
                  context={'categories':categories})


@login_required()
def category_page(request, category):
    get_object_or_404(Category, slug=category)
    words =  RuToEng.objects.filter(category__name=category).annotate(
        is_favorite=Exists(
            Favorite.objects.filter(
                word=OuterRef("pk"),
                user=request.user
            )
        )
    )
    return render(request, 'category.html', context={"words":words, "category": category})


@login_required()
def dictionary_list(request):
    words = RuToEng.objects.all()
    letter_dict = defaultdict(list)
    for word in words:
        letter_key = word.eng_word.word[0].upper()
        letter_dict[letter_key].append(word)

    return render(request, 'dict.html', context={'letter_dict':dict(letter_dict)})


@login_required()
def add_to_fav(request):
    if request.method == "POST":
        fav_words = request.POST.getlist('words')
        Favorite.objects.bulk_create([Favorite(word_id=i, user=request.user) for i in fav_words], ignore_conflicts=True)
        return redirect("user:profile")



@login_required()
def rm_from_fav(request):
    if request.method == "POST":
        unfav_words = request.POST.getlist('words')
        Favorite.objects.filter(user=request.user, id__in=unfav_words).delete()
        return redirect("user:profile")
    

@login_required()
def add_word(request):
    form = AddWordForm(request.POST or None)
    if form.is_valid():
        rus_w = form.cleaned_data['rus_version']
        eng_w = form.cleaned_data['eng_version']
        category_name = form.cleaned_data['category']
        ru_obj, _ = RusVersion.objects.get_or_create(word=rus_w)
        eng_obj, _ = EngVersion.objects.get_or_create(word=eng_w)
        post, _ = RuToEng.objects.get_or_create(ru_word=ru_obj, eng_word=eng_obj)
        post.category.add(*category_name)
        return redirect("dictionaryapp:word_page", post.id)
    return render(request, 'addwordform.html', {"form":form})


@login_required()
def word_page(request, pk):
    word = get_object_or_404(RuToEng, id=pk)
    english_word = word.eng_word.word
    all_translates = RuToEng.objects.filter(eng_word__word=english_word)
    fav_list = Favorite.objects.filter(user=request.user).values_list('word_id', flat=True)
    return render(request, 'trans_page.html',
                  {'word': word, 'fav_list': fav_list, 'all_translates': all_translates})
