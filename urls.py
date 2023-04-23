"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from .views import home, signup, blog_post, HomeView


"""Méthode CBV"""
urlpatterns = [
    path('', HomeView.as_view(title="Accueil du site"), name="home"),
    path('about/', HomeView.as_view(title="A propos"), name="about"),
    path('blog/', include("blog.urls")),
    path('signup/', signup, name="signup"),
    path('article/', blog_post, name="add_post"),
    path('custom-admin/', admin.site.urls),
]

"""
Méthode FBV
urlpatterns = [
    path('blog/', include("blog.urls")),
    path('signup/', signup, name="signup"),
    path('article/', blog_post, name="add_post"),
    path('custom-admin/', admin.site.urls),
]
"""
