from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.utils.crypto import get_random_string

CATEGORY_CHOICES = (
    ('p','NEWS'),
    ('y','YOUTH'),
    ('e','ENTERTAINMENT'),
    ('c','GAMES'),
    ('t','WORLD'),
    ('r','REVIEWS'),
)

REVIEWS_CHOICES = (
    (' ',' '),
    ('MOVIES','MOVIES'),
    ('SERIES','SERIES'),
)

class News(models.Model):
    title = models.CharField(max_length=500)
    short_desc = models.CharField(max_length=1000)
    image = models.CharField(max_length=500)
    decription = models.TextField(max_length=5000)
    youtube = models.CharField(max_length=1000,blank=True)
    description = models.TextField(max_length=5000,blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES , max_length=1 , default=0)
    created = models.DateTimeField(default=timezone.now)
    reviews_tag = models.CharField(choices=REVIEWS_CHOICES, max_length=6, default=0)

    slug = models.SlugField(max_length=50,unique=True)

    
    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=500)
    image_size_950x280 = models.CharField(max_length=500)
    slug = models.SlugField(max_length=50,unique=True)

    def __str__(self):
        return self.title

class trending(models.Model):
    title = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    slug = models.SlugField(max_length=50,unique=True)
    
    def __str__(self):
        return self.title

class read(models.Model):
    title = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    slug = models.SlugField(max_length=50,unique=True)

    def __str__(self):
        return self.title
