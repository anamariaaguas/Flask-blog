from django.contrib import admin
from django.urls import path

from newsproject.newsapp import views

#from newsproject.newsapp import views

#from newsapp import views

urlpatterns = [
   path('', views.index, name ='index'),
    path('admin/', admin.site.urls),
]