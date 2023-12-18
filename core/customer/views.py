
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.customer import forms
from django.urls import reverse





@login_required()
def home(request):
    return redirect(reverse("customer:profile"))

@login_required(login_url="/sign-in/?next=/customer/")
def profile_page(request):
    user_form = forms.BasicUserForm(instance=request.user)

    if request.method=="POST":
        user_form=forms.BasicUserForm(request.POST,instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse("customer:profile"))


    return render(request,'customer/profile.html',{
        "user_form":user_form
    })


