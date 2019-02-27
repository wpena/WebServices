from django.urls import path
from .views import (
    StoryListView, StoryDetailView, StoryCreateView,
    StoryDeleteView
    )
from . import views

urlpatterns = [
    path('', StoryListView.as_view(), name='news-home'),
    path('api/getstories/<int:pk>/', StoryDetailView.as_view(), name='story-detail'),
    path('api/poststory/', StoryCreateView.as_view(), name='story-create'),
    path('api/<int:pk>/deletestory/', StoryDeleteView.as_view(), name='story-delete'),
    path('author/', views.author, name='news-author'),
]