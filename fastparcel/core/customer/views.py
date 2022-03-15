
from django.urls import reverse
from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from core.customer import forms
# Create your views here.

#redirects to customer profile
@login_required()
def home(request):
    return redirect(reverse('customer:profile'))

# required diffrerent login url
@login_required(login_url="/sign-in/?next=/customer/")
def profile_page(request):
    user_form = forms.BasicUserForm(instance=request.user)

    #update customer's name
    if request.method == "POST":
        user_form = forms.BasicUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse('customer:profile')) #redirect to profile


    return render(request, 'customer/profile.html', {
        "user_form" : user_form
    })