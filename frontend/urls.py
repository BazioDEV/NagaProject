# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Bazio
"""

from django.urls import path, re_path
from frontend import views

urlpatterns = [

    # The home page
    path('', views.index, name='HomePage'),

]
