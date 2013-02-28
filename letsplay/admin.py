from django.contrib import admin
from letsplay.models import AgeGroup, Category, Content, Background, Avatar

admin.site.register(Category)
admin.site.register(AgeGroup)
admin.site.register(Content)
admin.site.register(Background)
admin.site.register(Avatar)