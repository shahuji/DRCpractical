from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from accounts.views import RegistrationView, MyLogout, UserView

app_name = "accounts"

urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='signup'),
]
