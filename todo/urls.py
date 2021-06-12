from django.urls import path,include

from . import views

urlpatterns = [
    path('current',views.currenttodos,name='currenttodos'),
    path('create',views.createtodo,name='createtodo'),
    path('list/<int:todo_pk>',views.viewtodo,name='viewtodo'), #Listing the todo based on primary key (ID)
    path('list/<int:todo_pk>/complete',views.completetodo,name='completetodo'),
    path('list/<int:todo_pk>/delete',views.deletetodo,name='deletetodo'),
    path('completed',views.completedtodos,name='completedtodos'),
    path('list/<int:todo_pk>/removecompletedtodo',views.removecompletedtodo,name='removecompletedtodo'),
]

#Every link will come like 127.0.0.1/todo/current (etc.)
