from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('news', views.StoryView)
router.register('author', views.AuthorView)


urlpatterns = [
    path('', include(router.urls))

]
