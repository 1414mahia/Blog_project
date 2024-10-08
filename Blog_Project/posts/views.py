from django.shortcuts import render,redirect

from posts import models
from posts.models import Post
from  .import forms
# Create your views here.
def add_posts(request):
    if request.method =='POST':
        post_form =forms.PostForm(request.POST)
        if post_form.is_valid():
          post_form.save()
          return redirect("add_posts")
    else:
        post_form=forms.PostForm()
    return render(request,"add_post.html",{'form':post_form})

def edit_posts(request,id):
    
    post =models.Post.objects.get(pk=id)
    post_form =forms.PostForm(instance= post)
    
    if request.method =='POST':
        post_form =forms.PostForm(request.POST,instance=post)
        if post_form.is_valid():
          post_form.save()
          return redirect("home_page")
   
    return render(request,"add_post.html",{'form':post_form} )

def delete(request,id):
     post =models.Post.objects.get(pk=id)
     post.delete()
     return redirect("home_page")
   
     
    