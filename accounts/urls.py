from django.urls import path,include

from . import views

urlpatterns = [
    #Authentication
    path('signup',views.signup,name='signup'),
]
