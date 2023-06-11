from django.contrib import admin
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('<int:product_id>/', views.list_reviews, name='list_reviews'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    path('edit_review/<int:review_id>/',
         views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>',
         views.delete_review, name='delete_review'),
]
