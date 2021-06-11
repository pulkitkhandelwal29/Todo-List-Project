#Creating form
from django.forms import ModelForm

from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        #Accessing the class from models.py file
        model = Todo
        #Creating all the form fields that we want from models (these fields are defined in models.py file)
        fields = ['title','memo','important']
