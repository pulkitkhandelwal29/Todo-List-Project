from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'todo/index.html')

def currenttodos(request):
    return render(request,'todo/currenttodos.html')
