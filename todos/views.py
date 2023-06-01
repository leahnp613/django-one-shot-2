from django.shortcuts import render, redirect
from .models import TodoItem, TodoList
from .forms import TodoForm

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

def create_todo_list(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todolist = form.save()
            return redirect("todo_list_detail", id=todolist.id)
    else:
        form = TodoForm()
    context = {
        "form":form
    }
    return render(request, "create.html", context)

def update_todo_list(request, id):
    todo_list = TodoList.objects.get(id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance= todo_list)
        if form.is_valid():
            todo_list = form.save()
            return redirect("todo_list_detail", id=todo_list.id)
    else:
        form = TodoForm(instance=todo_list)
    context ={
        "form":form
    }
    return render(request, "edit.html", context)