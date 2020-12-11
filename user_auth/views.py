from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # if form.is_valid()
        user_name = form.cleaned_data.get('username')
    context = {
        "form":form
    }
    return render(request,'user_auth/register.html',context)