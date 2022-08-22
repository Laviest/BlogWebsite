from django.shortcuts import render, redirect
from .forms import RegisterForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'register/edit_profile.html'
    success_url = reverse_lazy('my_profile')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('my_profile')
