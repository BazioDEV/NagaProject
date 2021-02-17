from django.shortcuts import render
from datetime import datetime
from .models import carousel, card_promotion

# Create your views here.
def index(request):
    # function
    today = datetime.now()
    img_slide = carousel.objects.all()
    post = card_promotion.objects.all()
    return render(request, 'frontend/index.html', {'today':today, 'carousel':img_slide, 'card_promotion':post})


# def card(request):
#     today = datetime.now()
#     card_img = card_promotion.objects.all()
#     return render(request, 'includes/card.html', {'today':today, 'card_promotion':card_img})