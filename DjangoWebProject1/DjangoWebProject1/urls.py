"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
]
