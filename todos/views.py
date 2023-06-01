from django.shortcuts import render
from .models import TodoItem, TodoList

# Create your views here.
def todo_list_list(request):
    Todo_list_list = TodoList.objects.all()
    context = {
        "Todo_list_list": Todo_list_list
    }

    return render(request, "list.html", context)

def show_todos(request, id):
    list = TodoList.objects.get(id=id)
    context= {
        "list":list,
    }
    return render(request, "detail.html", context)