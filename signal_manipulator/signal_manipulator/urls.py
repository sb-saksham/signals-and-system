"""signal_manipulator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import step_view, impulse_view, cos_view, sin_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', step_view, name="step"),
    path('impulse/', impulse_view, name="impulse"),
    path('cos/', cos_view, name="cos"),
    path('sin/', sin_view, name="sin"),
]
