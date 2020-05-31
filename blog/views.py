from django.shortcuts import render, HttpResponse
from .models import Contactus, Post, Emails
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    allposts = Post.objects.all()
    paginator = Paginator(allposts, 3)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    context = {
        'allposts': page_obj.object_list,
        'paginator' : paginator,
        'page_obj' : page_obj
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


def privacypolices(request):
    return render(request, "privacypolices.html")


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