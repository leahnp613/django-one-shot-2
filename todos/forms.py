from django import forms 
from todos.models import TodoList


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = [
            "name",
        ]