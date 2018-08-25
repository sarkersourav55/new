from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .models import todo
from .forms import todoform,newform

def index(request):
    hello=todo.objects.order_by('id')
    new=newform()
    #form=todoform()
    context={'todolist':hello,'form':new}
    return render(request,'tdlist/todo.html',context)
@require_POST

def addtodo(request):
    asap=todo.objects.get(pk=25)
    form=newform(request.POST,instance=asap)
    
    if form.is_valid():
        #new=todo(text=form.cleaned_data['text'])
        #new.save()
        newf=form.save()

    return redirect('index')
def complete(request,todoid):
    newtoc=todo.objects.get(pk=todoid)
    newtoc.complete=True
    newtoc.save()
    
    return redirect('index')
def deletecompleted(request):
    todo.objects.filter(complete__exact=True).delete()

    return redirect('index')
def deleteall(request):
    todo.objects.all().delete()

    return redirect('index')

