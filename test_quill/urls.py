from django.urls import path,include
from .views import *


urlpatterns=[
    path('',Home, name='home'),
    path('add/',Add, name='add')
]
