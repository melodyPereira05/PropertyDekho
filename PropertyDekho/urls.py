"""PropertyDekho URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('routes.urls') , name="Route-app"),
    path('properties/', include('properties.urls'),name="Property-app"),
    path('accounts/' ,include('accounts.urls'),name="account-app") 
    #path('blog/', include('properties.urls'),name="Blog-app"),
    #path('servies/', include('services.urls'),name="Service-app"),
    #path('agents/', include('agents.urls'),name="Agent-app"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # reference -- https://docs.djangoproject.com/en/3.1/ref/urls/ ,useful in debug mode.

