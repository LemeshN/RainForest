from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_product/', views.add_product, name='add_product'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),
    path('product_detail/<int:id>/delete/', views.product_delete, name='product_delete'),
    path('product_detail/<int:id>/update/', views.update, name='update'),
    path('add_order/', views.add_order, name='add_order')
]
