from django.urls import path
from . import views  # import from current folder

urlpatterns = [
    path("", views.index)
]
