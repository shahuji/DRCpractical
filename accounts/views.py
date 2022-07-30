from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse

from django.views.generic import CreateView, View
from accounts.form import RegistrationForm

from accounts.models import Images
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your views here.


class RegistrationView(CreateView):
    model = get_user_model()
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:view')
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(
                request,
                username=username,
                password=raw_password
            )
            login(request, user)
            return redirect(reverse('accounts:view'))
        return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
