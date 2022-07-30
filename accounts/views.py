from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse

from django.views.generic import CreateView, View
from accounts.form import RegistrationForm, ImageUploadForm

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


class MyLogout(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, _("You have successfully logged out."))
        return super().dispatch(request, *args, **kwargs)


@login_required(login_url='accounts:login')
def viewUser(request):
    """Viewing perticular user details"""
    # Images.objects.get(user=pk) is not None
    pk = request.user.pk
    if Images.objects.filter(user_id=pk).exists():
        userImg = Images.objects.get(user_id=pk)
    else:
        userImg = "images/pro.png"
    context = {"data": userImg}
    return render(request, 'accounts/view.html', context)


class UserView(View):

    def get(self, request):
        form = ImageUploadForm()
        #
        # return render(request, 'home.html', context={'form':form})
        pk = request.user
        if Images.objects.filter(user=pk, is_active=1).exists():
            image_list = Images.objects.filter(user_id=pk, is_active=1)
            total_image = image_list.count()
        else:
            total_image = 0
            image_list = None
        context = {
            "image_list": image_list,
            "total_image": total_image,
            'form': form,
        }
        return render(request, 'accounts/view.html', context)

    def post(self, request):
        if request.method == 'POST':
            form = ImageUploadForm(request.POST, request.FILES)
            if form.is_valid():
                image = Images(**form.cleaned_data, user=request.user)
                image.save()
                return JsonResponse({'data': 'Data uploaded'})

            else:
                return JsonResponse({'data':'Something went wrong!!'})
