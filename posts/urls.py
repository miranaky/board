from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.PostsView.as_view()),
    path("<int:pk>", views.PostView.as_view()),
]
