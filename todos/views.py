from django.shortcuts import render
from .models import TodoList

# Create your views here.
def todo_list_list(request):
    TodoList_list = TodoList.objects.all()
    context = {
        "Todo_List_list": TodoList_list
    }

    return render(request, "todo_list_list.html", context)