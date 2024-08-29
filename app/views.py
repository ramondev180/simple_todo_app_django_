from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TodoList
from .forms import CreateTaskForm,EditTaskForm
# Create your views here.



@login_required(login_url='userauth:login')
def dashboard(request):
    all_lists = TodoList.objects.order_by("-id").all()
    form_errors = request.session.pop('form_errors', None)
    form_data = None if not form_errors else request.session.pop('form_data')
    form = CreateTaskForm(form_data) 
    context ={
        "all_lists": all_lists,
        'form' : form
    }
    return render(request,'dashboard.html',context=context) 


@login_required(login_url='userauth:login')
def edit_task(request, pk):
    context ={}
    try:
        todo_items = TodoList.objects.get(pk=pk)
        if request.method == 'POST':
            form = EditTaskForm(request.POST, instance=todo_items)
            context['form'] = form
            if form.is_valid():
                form.save()
                messages.success(request,"Task updated successfully")
                return redirect('app:dashboard')
            else:
                request.session['form_errors'] = form.errors
                request.session['form_data'] = form.cleaned_data

        context['item'] = todo_items

        return render(request,'edit-todo.html',context=context)
    
    except TodoList.DoesNotExist:
        messages.error(request,"Task not found")
        return redirect('app:dashboard')


@login_required(login_url='userauth:login')
@require_POST
def create_task(request):
    form = CreateTaskForm(request.POST)
    
    if form.is_valid():
        # title = request.POST.get('title')
        # item = TodoList.objects.create(title=title)
        form.save()
        messages.success(request,"Successfully add to the list")

    else:
        request.session['form_errors'] = form.errors
        request.session['form_data'] = request.POST

    referrer = request.META.get('HTTP_REFERER', 'dashboard/')
    return redirect(referrer)


@login_required(login_url='userauth:login')
def delete_task(request,pk):
    try:
        item = TodoList.objects.get(pk=pk)
        item.delete()
        messages.success(request,"Task deleted successfully")
        return redirect('app:dashboard')
    except TodoList.DoesNotExist:
        messages.error(request,"Task not found")

