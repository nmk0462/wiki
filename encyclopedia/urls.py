from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entry,name="entry"),
    path("search",views.search,name="search"),
    path("create",views.create,name="create"),
    path("save",views.save,name="save"),
    path("edit/<str:nm1>",views.edit,name="edit"),
    path("savededit",views.saveedit,name="saveedit"),
    path("randomp",views.randomp,name="randomp")
]
