from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.utils.crypto import get_random_string

CATEGORY_CHOICES = (
    ('p','POLITICS'),
    ('y','YOUTH'),
    ('e','ENTERTAINMENT'),
    ('c','COVID-19'),
    ('t','TRENDING'),
    ('r','REVIEWS'),
)

TRENDING_CHOICES = (
    ('td','TRENDING TODAY '),
    ('tp','TOP TRENDING'),
    ('no','None')
)

class News(models.Model):
    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=500)
    decription = models.TextField(max_length=2000)
    image1 = models.ImageField()
    image2 = models.ImageField()
    category = models.CharField(choices=CATEGORY_CHOICES , max_length=1 , default=0)
    trending = models.CharField(choices=TRENDING_CHOICES , max_length=2 , default=0) 
    created = models.DateTimeField(default=timezone.now)
    slider = models.BooleanField(default=False)

    slug = models.SlugField(max_length=5,blank=True,) # blank if it needs to be migrated to a model that didn't already have this 
  # ...
    def save(self, *args, **kwargs):
        #""" Add Slug creating/checking to save method. """
        slug_save(self) # call slug_save, listed below
        super(News, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.title


    # ...
def slug_save(obj):
    #A function to generate a 5 character slug and see if it has been used and contains naughty words."""
    if not obj.slug: # if there isn't a slug
        obj.slug = get_random_string(5) # create one
        slug_is_wrong = True  
        while slug_is_wrong: # keep checking until we have a valid slug
            slug_is_wrong = False
            other_objs_with_slug = type(obj).objects.filter(slug=obj.slug)
            if len(other_objs_with_slug) > 0:
                # if any other objects have current slug
                slug_is_wrong = True
            naughty_words = ['thesocialbugg','fuck']
            if obj.slug in naughty_words:
                slug_is_wrong = True
            if slug_is_wrong:
                # create another slug and check it again
                obj.slug = get_random_string(5)


