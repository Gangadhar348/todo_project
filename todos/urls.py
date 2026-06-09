from django.urls import path

from . import views


app_name = "todos"

urlpatterns = [
    path("", views.todo_list, name="list"),
    path("toggle/<int:todo_id>/", views.toggle_todo, name="toggle"),
    path("delete/<int:todo_id>/", views.delete_todo, name="delete"),
]
