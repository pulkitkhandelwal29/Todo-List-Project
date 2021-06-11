from django.urls import path,include

from . import views

urlpatterns = [
    path('current',views.currenttodos,name='currenttodos'),
    path('create',views.createtodo,name='createtodo'),
]
