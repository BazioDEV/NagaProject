from django.shortcuts import render
from datetime import datetime
from .models import carousel, card_promotion

# Create your views here.
def index(request):
    # function
    today = datetime.now()
    img_slide = carousel.objects.all()
    return render(request, 'frontend/index.html', {'today':today, 'carousel':img_slide})

def card(request):
    today = datetime.now()
    data = card_promotion.objects.all()
    cdt = {
       'card_promotion':data
    }
    return render(request, 'includes/card.html', cdt, {'today':today})