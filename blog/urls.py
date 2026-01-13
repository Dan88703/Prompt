# blog/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import PostListView, PostDetailView, contact_view

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('kontakt/', contact_view, name='contact'),
]

