from django.urls import path, include

from . import views
from .components.comment import CommentView

app_name = "component"
urlpatterns = [
    path("", include("django_unicorn.urls")),
    path("", views.index, name="index"),
    path("", CommentView.as_view()),
]
