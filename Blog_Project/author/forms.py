from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = '__all__'
       # fields =['name','phn_no','bio']
        #exclude =['bio'] bio bad