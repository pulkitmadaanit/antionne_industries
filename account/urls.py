from django.urls import path
from account import views

urlpatterns = [
    path('',views.testing,name="home"),
    path('singleblog/',views.blog,name="blog-single"),
    # path('error404/',views.error404,name="error-404"),
]