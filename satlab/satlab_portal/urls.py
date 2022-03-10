from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('post/', views.postfeed, name="Post"),
    path('feed/', views.feed, name="Feed")
]