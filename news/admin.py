from django.contrib import admin
from news.models import News, Slider, read, trending

admin.site.register(News)
admin.site.register(Slider)
admin.site.register(read)
admin.site.register(trending)