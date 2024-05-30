from django.urls import path
from . import views

# Define a list of url patterns
urlpatterns = [
    path('', views.index)
]
