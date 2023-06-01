from django.urls import path
from todos.views import (
    create_todo_item,
    delete_todo_list,
    todo_list_list,
    show_todos,
    create_todo_list,
    update_todo_item,
    update_todo_list,
)

urlpatterns = [
    path("", todo_list_list, name="todo_list_list"),
    path("<int:id>/", show_todos, name="todo_list_detail"),
    path("create/", create_todo_list, name="todo_list_create"),
    path("<int:id>/edit/", update_todo_list, name="todo_list_update"),
    path("<int:id>/delete/", delete_todo_list, name="todo_list_delete"),
    path("item/create/", create_todo_item, name= "todo_item_create"),
    path("item/update/<int:id>", update_todo_item, name="todo_item_update"),

]
