from django.shortcuts import render,HttpResponseRedirect
from .models import TodoListItem 
# Create your views here.

def todoappView(request):
    return render(request, 'todolist.html')


def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items}) 

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/') 

def deleteTodoView( request,id):
    y = TodoListItem.objects.get(id=id)
    y.delete()
    return HttpResponseRedirect('/todoapp/') 

