from django.shortcuts import render,redirect,get_object_or_404

#Forms created using django, importing the class name
from .forms import TodoForm

#Importing Todo from models to access all the todos created
from .models import Todo

from django.utils import timezone #Importing timezone to set datecompleted to NULL (fix the time as the curent time)

#Does not allow user to access page until user is logged in
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'todo/index.html')

@login_required
def currenttodos(request):
    #Accessing all todos for specific user that are in database
    #If the user clicks on completed that todo, it should not appear there (this is how it is a filter)
    todos = Todo.objects.filter(user = request.user , datecompleted__isnull = True)
    return render(request,'todo/currenttodos.html',{'todos':todos})

@login_required
def createtodo(request):
    #If createtodo link is opened, it's a GET request
    if request.method == 'GET':
        return render(request,'todo/createtodo.html',{'form':TodoForm()})
    else:
        #Put all the details recevied from webapge in TodoForm
        form = TodoForm(request.POST)
        #Save it but do not save right now in database(as user field is right now empty,we want the user to be attached)
        newtodo = form.save(commit = False)
        #Setting user to the user that is logged in
        newtodo.user = request.user
        #Now finally save it in database
        newtodo.save()
        #After saving todos, redirecting to the currenttodo webpage, where it can see its todos
        return redirect('currenttodos')

#Viewing todo based on Primary key
@login_required
def viewtodo(request,todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user) #accessing those todos only created by the specific user(prevent from someone just try to access todos by changing ID above in URL)
    if request.method == 'GET':
        form = TodoForm(instance=todo) #Calling the form with details already in it using instance of above todo
        return render(request,'todo/viewtodo.html',{'todo':todo,'form':form})
    else:
        #Save the updated details
        form = TodoForm(request.POST,instance=todo) #Referring the instance of todo only that has saved info
        #Directly saving as no need to define which user
        form.save()
        return redirect('currenttodos')

@login_required
def completetodo(request,todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        #Setting datecompleted field to the current time leading to becoming it NULl
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currenttodos')

@login_required
def deletetodo(request,todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodos')

@login_required
def completedtodos(request):
    #Accessing all todos for specific user that are in database
    #If the user wants to see completed todo, it should appear there (this is how it is a filter)
    #Ordering in descending order (latest to not so latest) (using - sign)
    todos = Todo.objects.filter(user = request.user , datecompleted__isnull = False).order_by('-datecompleted')
    return render(request,'todo/completedtodos.html',{'todos':todos})

@login_required
def removecompletedtodo(request,todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user) #accessing those todos only created by the specific user(prevent from someone just try to access todos by changing ID above in URL)
    if request.method == 'GET':
        form = TodoForm(instance=todo) #Calling the form with details already in it using instance of above todo
        return render(request,'todo/removecompletedtodo.html',{'todo':todo,'form':form})
