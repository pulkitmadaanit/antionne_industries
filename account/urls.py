from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    # path('', views.HomeView.as_view(), name="home"),
    path('singleblog/', views.blog,name="blog-single"),
    # path('error404/',views.error404,name="error-404"),
    path('contact/', views.contact_us,name="contact"),
    path('about/', views.about_us,name="about"),

]