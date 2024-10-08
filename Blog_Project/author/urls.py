from django.urls import path,include

from author import views

urlpatterns = [
    path('',views.add_author,name='add_author'),
   
    
]
