from django.shortcuts import render
from .models import TodoList
# Create your views here.
def index(request):
    todo_items = TodoList.objects.order_by('id')
    context = {'todo_items': todo_items}
    return render(request, 'todoList/index.html', context) 