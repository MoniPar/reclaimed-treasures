from django.contrib import admin
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('<int:product_id>/', views.list_reviews, name='list_reviews'),
    path('add/<int:product_id>/', views.add_review, name='add_review'),
]
