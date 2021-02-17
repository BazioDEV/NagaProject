from django.db import models
from django.db.models.fields import CharField


# Create your models here.
class carousel(models.Model):
    title = models.CharField(max_length=100)
    carousel = models.ImageField(null = True, blank = True, upload_to ='carousel-img' )
    create_date = models.DateTimeField()

def image_thumb(self):
    return '<img src="/media/%s" width="100" height="100" />' % (self.photo)
image_thumb.allow_tags = True

class card_promotion(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    card_img = models.ImageField(null = True, blank = True, upload_to = 'card-img')
    create_date = models.DateTimeField()

def card_thumb(self):
    return '<img src="/media/%s" width="100" height="100" />' % (self.photo)
image_thumb.allow_tags = True

class feature(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    card_img = models.ImageField()
    create_date = models.DateTimeField()

def feature_thumb(self):
    return '<img src="/media/%s" width="100" height="100" />' % (self.photo)
image_thumb.allow_tags = True