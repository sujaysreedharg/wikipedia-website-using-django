from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create,name="create"),
    path("wiki/<str:title>", views.title, name="entry"),
    path("edit/<str:title>",views.edit,name="edit"),
    path("search",views.search,name="search"),
    path("random",views.randompage,name="random") 
]
