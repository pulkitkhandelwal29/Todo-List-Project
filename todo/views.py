from django.shortcuts import render,redirect

from .forms import TodoForm

# Create your views here.
def home(request):
    return render(request,'todo/index.html')

def currenttodos(request):
    return render(request,'todo/currenttodos.html')

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
