from . import views
from django.urls import path
from .feeds import LatestPostsFeed


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),#Se crea una ruta para la lista de post
    path("about_me/", views.AboutMe.as_view(), name="about_me"),#Se crea una ruta para el about me
    path("<slug:slug>/", views.post_detail, name="post_detail"),#Se crea una ruta para el detalle del post
    path("feed/rss", LatestPostsFeed(), name="post_feed"),#Se crea una ruta para el feed de los post
    
    

]