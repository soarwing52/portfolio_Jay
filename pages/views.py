from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request,"home.html", {})

def contact_view(request,*args, **kwargs):
    return render(request,"map.html", {})

def about_view(request, *args, **kwargs):
    my_content = {
        "my_text":'text in a dic',
        "my_number":12154,
        "my_list":['sdf','ASDf','rtqrew',123]
    }
    return render(request,"about.html", my_content)
