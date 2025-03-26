from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wordsApp.urls', namespace='dictionaryapp')),
    path('trainer/', include('trainerapp.urls', namespace='trainerapp')),
    path('user/', include('user.urls', namespace='user')),

]

