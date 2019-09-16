from django.urls import path
from . import views

urlpatterns = [    
    path('produto/', views.home),
    path('produto/show/<int:id>', views.produto_show),
    path('produto/list', views.produto_list),
    path('produto/create/', views.create),
    
]