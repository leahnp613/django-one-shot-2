from django.urls import path
from todos.views import todo_list_list, show_todos

urlpatterns = [
    path("", todo_list_list, name="todolist_list"),
    path("/<int:id>/", show_todos, name ="todo_list_detail"),
]