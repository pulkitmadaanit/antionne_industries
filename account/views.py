from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
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
=======
from django.views.generic import TemplateView
from account.models import *
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import View
>>>>>>> ed25623dc771bf5e0c84c3a5dc393f168f990fd5



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


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        mess = request.POST.get("message")
<<<<<<< HEAD
        print(name,email,phone)
=======
       
        print(name,email,phone)
        
>>>>>>> ed25623dc771bf5e0c84c3a5dc393f168f990fd5
        send_mail(
            subject,
            mess,
            email,
            [settings.EMAIL_HOST_USER]
        )
<<<<<<< HEAD
        # Send email wit htlms
        html_content = render_to_string('account/mail.html', context)
=======
        
        html_content = render_to_string('account/mail.html', context)

>>>>>>> ed25623dc771bf5e0c84c3a5dc393f168f990fd5
        return HttpResponse("Done")
    else:
        return render(request, "account/contact.html")


def about_us(request):
    return render(request, "account/aboutus.html")


# ---------------------------Productone------------------------------------------------------
"""  Class Based View Productone """
class ProductOneView(View):
    def get(self, request):
        template_name = "account/products/Productone/one.html" 
        return render(request, template_name)

class ProductTwoView(View):
    def get(self, request):
        template_name = "account/products/Productone/two.html" 
        return render(request, template_name)

class ProductThreeView(View):
    def get(self, request):
        template_name = "account/products/Productone/three.html" 
        return render(request, template_name)

class ProductFourView(View):
    def get(self, request):
        template_name = "account/products/Productone/four.html" 
        return render(request, template_name)

""" END product one """  
# -----------------------------end Productone----------------------------------------------------


# ---------------------------------Producttwo------------------------------------------------

product_path2 = "account/products/Producttwo/"

def product2_product1(request):
    return render(request,product_path2 + 'one.html' )

def product2_product2(request):
    return render(request,product_path2 + "two.html" )

def product2_product3(request):
    return render(request,product_path2 + "three.html" )

def product2_product4(request):
    return render(request,product_path2 + "four.html" )

# ----------------------------------end Producttwo-----------------------------------------------


# --------------------------------Productthree-------------------------------------------------

product_path3 = "account/products/Productthree/"

def product3_product1(request):
    return render(request,product_path3 + "one.html" )

def product3_product2(request):
    return render(request,product_path3 + "two.html" )

def product3_product3(request):
    return render(request,product_path3 + "three.html" )

def product3_product4(request):
    return render(request,product_path3 + "four.html" )

# ----------------------------------end Productthree-----------------------------------------------


# ----------------------------------Productfour-----------------------------------------------

product_path4 = "account/products/Productfour/"

def product4_product1(request):
    return render(request,product_path4 + "one.html" )

def product4_product2(request):
    return render(request,product_path4 + "two.html" )

def product4_product3(request):
    return render(request,product_path4 + "three.html")

def product4_product4(request):
    return render(request,product_path4 + "four.html")

# ---------------------------------end productfour------------------------------------------------




