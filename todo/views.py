from django.shortcuts import render,redirect,get_object_or_404

from .forms import TodoForm

#Importing Todo from models to access all the todos created
from .models import Todo

# Create your views here.
def home(request):
    return render(request,'todo/index.html')

def currenttodos(request):
    #Accessing all todos for specific user that are in database
    #If the user clicks on completed that todo, it should not appear there (this is how it is a filter)
    todos = Todo.objects.filter(user = request.user , datecompleted__isnull = True)
    return render(request,'todo/currenttodos.html',{'todos':todos})

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
def viewtodo(request,todo_pk):
    todo = get_object_or_404(Todo,pk=todo_pk)
    return render(request,'todo/viewtodo.html',{'todo':todo})
