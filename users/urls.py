from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.UsersView.as_view()),
    path("me", views.me_view),
    path("<int:pk>", views.user_view),
    path("login", views.login),
]
