from django.urls import path,include

from . import views

urlpatterns = [
    path('current',views.currenttodos,name='currenttodos'),
    path('create',views.createtodo,name='createtodo'),
    path('list/<int:todo_pk>',views.viewtodo,name='viewtodo'), #Listing the todo based on primary key (ID)
]
