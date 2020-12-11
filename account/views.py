from django.shortcuts import render
from django.http import HttpResponse
# from django.views.generic import TemplateView
from .models import *
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

# class HomeView(TemplateView):
#     model = HomeSlider
#     template_name = "account/index.html"



def home(request):
    home_slider   = HomeSlider.objects.all()
    client_slider = ClientSlider.objects.all()
    product_data  = Product.objects.all()[:3]
   


    context = {
        "home_slider": home_slider,
        "client_slider":client_slider,
        "product_data": product_data,
    }
    return render(request, "account/index.html", context)

def blog(request):
    return render(request, "account/blog-single.html")

def error404(request):
    return render(request, "account/404.html")


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        mess = request.POST.get("message")
        print(name,email,phone)
        send_mail(
            subject,
            mess,
            email,
            [settings.EMAIL_HOST_USER]
        )
        # --------------------------------------
        html_content = render_to_string('account/mail.html', context)
        return HttpResponse("Done")
    else:
        return render(request, "account/contact.html")


def about_us(request):
    return render(request, "account/aboutus.html")