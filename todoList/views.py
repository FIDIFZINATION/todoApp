from django.shortcuts import redirect, render

from .models import TodoList
from .forms import TodoListForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    todo_items = TodoList.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_items': todo_items, 'form': form}
    return render(request, 'todoList/index.html', context) 

@require_POST
def addItem(request):
    form = TodoListForm(request.POST)

    if form.is_valid():
        new_task = TodoList(task=request.POST['text'])
        new_task.save()    

    return redirect('index')

def completedTask(request, todo_id):
    todo = TodoList.objects.get(pk=todo_id)
    todo.status = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):   
    TodoList.objects.filter(status__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    TodoList.objects.all().delete()

    return redirect('index')