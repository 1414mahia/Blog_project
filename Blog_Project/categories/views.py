from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_categories(request):
    if request.method =='POST':
        
      category_form =forms.CategoryForm(request.POST) # form class er AuthorFrom
      if  category_form.is_valid(): # user er post valid kina  check korbe
           category_form.save() # valid hoihe save korbe
           return redirect("add_categories")
    else:
       category_form =forms.CategoryForm() # user website a dhukche but kono data pass kore nai,blank form pabe
    return render(request,'add_category.html',{'form': category_form})