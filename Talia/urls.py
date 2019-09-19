from django.urls import path
from . import views

urlpatterns = [    
    path('produto/', views.home),
    path('produto/show/<int:id>', views.produto_show),
    path('produto/list', views.produto_list),
    path('produto/create/', views.produto_form),
    path('produto/editar/<int:produto_id/>', views.produto_editar),
    path('produto/delete/<int:produto_id/>', views.produto_delete),
    
    path('cliente/', views.home),
    path('cliente/show/<int:id>', views.cliente_show),
    path('cliente/list', views.cliente_list),
    path('cliente/create/', views.cliente_form),
    path('cliente/editar/<int:cliente_id/>', views.cliente_editar),
    path('cliente/delete/<int:cliente_id/>', views.cliente_delete),

    path('carrinho/', views.home),
    path('carrinho/show/<int:id>', views.carrinho_show),
    path('carrinho/list', views.carrinho_list),
    path('carrinho/create/', views.carrinho_form),
    path('carrinho/editar/<int:carrinho_id/>', views.carrinho_editar),
    path('carrinho/delete/<int:carrinho_id/>', views.carrinho_delete),
    
]