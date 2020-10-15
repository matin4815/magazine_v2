from django.db import models
from datetime import datetime
#from writers.models import Writer
from taggit.managers import TaggableManager
from django.db.models.signals import pre_save
from magazine_v2.utils import unique_slug_generator


class Article(models.Model):
 # writer = models.ForeignKey(Writer, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=150)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  article_date = models.DateTimeField(default=datetime.now, blank=True)
  body1 = models.TextField()
  body2 = models.TextField(blank=True)
  body3 = models.TextField(blank=True)
  quote1 = models.TextField(blank=True)
  quote2 = models.TextField(blank=True)
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  is_published = models.BooleanField(default=True)
  slug = models.SlugField(unique=True, max_length=100, null=True, blank=True)
  tags = TaggableManager()

  def __str__(self):
    return self.title

def slug_generator(sender, instance, *args, **kwargs):
  if not instance.slug:
    instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Article)