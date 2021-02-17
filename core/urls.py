# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Bazio
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('frontend.urls')),
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
    path("dashboard/", include("app.urls"))             # UI Kits Html files
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

