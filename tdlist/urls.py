from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('add',views.addtodo,name='add'),
    path('complete/<todoid>',views.complete,name='complete'),
    path('completed',views.deletecompleted,name='completed'),
    path('all',views.deleteall,name='all')
]