from django.shortcuts import redirect, render
from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    total_tasks = tasks.count()

    completed_tasks = Task.objects.filter(completed = True)
    completed_tasks_count = completed_tasks.count()

    incompleted_tasks = Task.objects.filter(completed = False)
    incompleted_tasks_count = incompleted_tasks.count()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/')
    else:
        form = TaskForm()

    context = {
        'tasks' : tasks,
        'total_tasks' : total_tasks,
        'completed_tasks_count' : completed_tasks_count,
        'incompleted_tasks_count' : incompleted_tasks_count,
        'form' : form,
    }
    return render(request,'main/home.html',context)

def update(request,pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect('/')
    else:
        form = TaskForm(instance=task)
    
    context = {
        'task' : task,
        'form': form,
    }

    return render(request, 'main/edit.html', context)

def delete(request,pk):
    task = Task.objects.filter(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    
    context = {
        'task' : task,
    }

    return render(request,'main/delete.html',context)