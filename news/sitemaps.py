from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from news.models import News


class StaticSitemap(Sitemap):

    def items(self):
        return ['thesocialbugg']

    def location(self, item):
        return reverse(item)

class FullwidthSitemap(Sitemap):

    def items(self):
        return News.objects.all()

    def location(self, item):
        return reverse('fullwidth', args=[item.slug])
