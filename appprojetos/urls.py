from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('projetos/', views.paginaProjeto, name='projetos'),  
    path('boutique/', views.primeirapaginaluchesy, name='boutique'),
]