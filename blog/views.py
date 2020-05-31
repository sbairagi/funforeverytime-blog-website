from django.shortcuts import render, HttpResponse
from .models import Contactus, Post, Emails
from django.contrib import messages


# Create your views here.
def home(request):
    allposts = Post.objects.all()
    context = {
        'allposts': allposts
    }
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        name_email_msg = Contactus.objects.filter(name=name,email=email,msg=msg)
        if name_email_msg:
            messages.success(request, "your contact detail has been sent successfully")
            return render(request, "index.html")
        else:
            contactus = Contactus(name=name, email=email, msg=msg)
            contactus.save()
            messages.success(request, "your contact detail has been sent successfully")

    return render(request, "index.html",context)


def blogs(request):
    return render(request, "blogs.html")


def aboutus(request):
    return render(request, "aboutus.html")


def contactus(request):
    return render(request, "contactus.html")

def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    context = { 'post' : post }
    return render(request, "post.html" , context)