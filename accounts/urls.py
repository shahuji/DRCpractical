from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from accounts.views import RegistrationView, MyLogout, UserView

app_name = "accounts"

urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='login'),

    path('logout/',
         MyLogout.as_view(template_name='accounts/logout.html'),
         name='logout'),
    path('view/', login_required(UserView.as_view()), name='view'),
]
