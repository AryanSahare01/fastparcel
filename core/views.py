from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import forms


def home(request):  
    return render(request, 'home.html')

@login_required()
def customer_page(request):
    return render(request, 'customer.html')

@login_required()
def courier_page(request):
    return render(request, 'courier.html')

def sign_up(request):
    form = forms.SignUpForm()
    return render(request, 'sign_up.html', {'form': form})



