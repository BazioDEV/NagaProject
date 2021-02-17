from django.contrib import admin
from .models import carousel, card_promotion, feature


# Register your models here.
class carouselAdmin(admin.ModelAdmin):
    list_display = ('id','title','carousel', 'create_date',)

def image_thumb(self):
    return '<img src="/media/%s" width="100" height="100" />' % (self.photo)
image_thumb.allow_tags = True

class cardAdmin(admin.ModelAdmin):
    licst_display = ('id', 'title', 'description', 'card_img', 'careate_date')

def __str__(self):
    return self.title


# Register Admin 
admin.site.register(carousel, carouselAdmin)
admin.site.register(card_promotion, cardAdmin)

