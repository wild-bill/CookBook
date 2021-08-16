from django.urls import path
from . import views


urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('recipe/<int:pk>/', views.post_detail, name='post_detail'),
    path('recipe/new/', views.post_new, name = 'post_new'),
    path('recipe/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
