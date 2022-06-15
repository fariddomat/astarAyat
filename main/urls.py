from django.urls import path
from . import views

urlpatterns = [
    path("", views.addRomania, name="addRomania"),
    path("search", views.search, name="search"),
    path("addCountry", views.addCountry, name="addCountry"),
    
    
]
