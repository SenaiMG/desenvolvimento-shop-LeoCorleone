from django.urls import path 
from . import views 


urlpatterns = [
    path("", views.index, name="index"),
    path("carrinho", views.carrinho, name='carrinho'),
    path("produtos", views.produtos, name='produtos'),
    path("adicionar", views.adicionar, name='adicionar'),
]