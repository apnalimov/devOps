from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
# from django.http import HttpResponse
from .models import ToDo

# Create your views here.
def index(request):
    todos = ToDo.objects.all()
    return render(request, 'toDoApp/index.html', {'todos' : todos})


@require_http_methods(['POST'])
# def add(request):
#     title = request.POST['title']
#     todo = ToDo(title=title)
#     todo.save()
#     return redirect('index')


def add(request):
    title = request.POST['title']
    body = request.POST['body']
    open_date = request.POST['open_date']
    control_date = request.POST['control_date']
    todo = ToDo(title=title, body=body, open_date=open_date, control_date=control_date)
    todo.save()
    return redirect('index')


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')