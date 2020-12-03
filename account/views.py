from django.shortcuts import render

# Create your views here.
def testing(request):
    return render(request, "account/index.html")

def blog(request):
    return render(request, "account/blog-single.html")

def error404(request):
    return render(request, "account/404.html")

def contact_us(request):
    return render(request, "account/contact.html")


def about_us(request):
    return render(request, "account/aboutus.html")