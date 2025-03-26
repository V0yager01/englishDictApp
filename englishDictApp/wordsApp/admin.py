from django.contrib import admin

from .models import RuToEng, RusVersion, EngVersion, Category

from user.models import MyUser, Profile


admin.site.register(Category)
admin.site.register(RuToEng)
admin.site.register(RusVersion)
admin.site.register(EngVersion)
admin.site.register(MyUser)
admin.site.register(Profile)