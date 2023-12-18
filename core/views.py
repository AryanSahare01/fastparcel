from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View 
from .models import MenuItem,Category,OrderModel
from . import forms


def home(request):  
    return render(request, 'home.html')



def sign_up(request):
    form = forms.SignUpForm()

    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email').lower()
            
            user = form.save(commit=False)
            #user.username = email
            user.save()

            login(request, user)
            return redirect('/')

    return render(request, 'sign_up.html', {'form': form})




class Order(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        appetizers = MenuItem.objects.filter(
            category__name__contains='Appetizer')
        entres = MenuItem.objects.filter(category__name__contains='Entre')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')

        # pass into context
        context = {
            'appetizers': appetizers,
            'entres': entres,
            'desserts': desserts,
            'drinks': drinks,
        }

        # render the template
        return render(request, 'customer/order.html', context)
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        HostelName = request.POST.get('HostelName')
        RoomNumber = request.POST.get('RoomNumber')

        order_items = {
            'items': []
        }


        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            price=price,
            HostelName=HostelName,
            RoomNumber=RoomNumber)
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price
        }

        return render(request, 'customer/order_confirmation.html', context)
    
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')