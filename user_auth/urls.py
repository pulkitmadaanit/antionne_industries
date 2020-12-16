from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('register/', views.user_register,name="register"),
=======
    path('register', views.user_register,name="register"),
>>>>>>> ed25623dc771bf5e0c84c3a5dc393f168f990fd5
    
]