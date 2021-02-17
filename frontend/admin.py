from django.contrib import admin
from .models import carousel, card_promotion, feature


# Register your models here.
class carouselAdmin(admin.ModelAdmin):
    list_display = ('id','title','carousel', 'create_date',)

def __str__(self):
    return self.title


class cardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'card_img', 'create_date')

def __str__(self):
    return self.title


# Register Admin 
admin.site.register(carousel, carouselAdmin)
admin.site.register(card_promotion, cardAdmin)

