"""goceylon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

from catalogue.views import (
    catalogue_view,
)

from ocr.views import (
    ocr_dashboard_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='catalogue-view', permanent=True)),
    path('catalogue/', catalogue_view, name='catalogue-view'),
    path('translate/', ocr_dashboard_view, name='ocr-dashboard'),
]
