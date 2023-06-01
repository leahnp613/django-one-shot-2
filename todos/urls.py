from django.urls import path
from todos.views import delete_todo_list, todo_list_list, show_todos, create_todo_list, update_todo_list

urlpatterns = [
    path("", todo_list_list, name="todolist_list"),
    path("<int:id>/", show_todos, name ="todo_list_detail"),
    path("create/", create_todo_list, name = "todo_list_create"),
    path("<int:id>/edit/", update_todo_list, name = "todo_list_update"),
    path("<int:id>/delete/", delete_todo_list, name= "todo_list_delete"),
]