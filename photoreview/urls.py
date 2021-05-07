from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="photoreview"),
    path('<str:id>', detail, name="photoreview/detail"),
    path('new/', new, name="photoreview/new"),
    path('create/', create, name="photoreview/create"),
    path('edit/<str:id>', edit, name="photoreview/edit"),
    path('update/<str:id>', update, name="photoreview/update"),
    path('delete/<str:id>', delete, name="photoreview/delete"),
]