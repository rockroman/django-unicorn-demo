from django.urls import path, include

from . import views

app_name = "component"
urlpatterns = [
    path("", include("django_unicorn.urls")),
    path("", views.index, name="index"),
]
