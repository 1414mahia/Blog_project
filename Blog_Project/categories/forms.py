from django import forms
from .models import  Category

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model =  Category
        fields = '__all__'
       # fields =['name','phn_no','bio']
        #exclude =['bio'] bio bad