from django.urls import path

from products import views

urlpatterns = [
    path('products/<int:product_id>/', views.product_details, name='product_detail')
]