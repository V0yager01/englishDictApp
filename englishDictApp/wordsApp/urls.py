from django.contrib import admin
from django.urls import path

from . import views

app_name = 'dictionaryapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category>/', views.category_page, name='category'),
    path('dictionary/', views.dictionary_list, name='dictionary_list'),
    path('add/', views.add_to_fav, name='fav'),
    path('rmfav/', views.rm_from_fav, name='fav_del'),
    path('add_word/', views.add_word, name='add_word'),
    path('word/<int:pk>/', views.word_page, name='word_page')
    
]
