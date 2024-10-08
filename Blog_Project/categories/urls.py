from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.add_categories,name='add_categories'), # views . function er nam
   # name er por j nam dibo ta diye html a url call korbo
   
                
]
