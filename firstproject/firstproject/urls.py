from django.urls import path
from . import views

urlpatterns = [
    path("api/yourmodel/", views.get_your_model, name="get_your_model"),
]
