from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),#Se crea una ruta para la lista de post
    path("<slug:slug>/", views.post_detail, name="post_detail"),#Se crea una ruta para el detalle del post
    
]