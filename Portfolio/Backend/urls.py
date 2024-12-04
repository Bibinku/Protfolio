from django.urls import path
from Backend import views

urlpatterns=[

    path('', views.indexpage, name="indexpage"),

]