from django.contrib import admin
from news.models import News,Slider,top_trending,trending_today

admin.site.register(News)
admin.site.register(Slider)
admin.site.register(top_trending)
admin.site.register(trending_today)