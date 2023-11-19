from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def customer_page(request):
    return render(request, 'customer.html')

def courier_page(request):
    return render(request, 'courier.html')



