from django.urls import path
from .views import RegistrationView, UserLogin, UserLogout, home


urlpatterns = [
    path('', home, name='home'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', UserLogin.as_view(),  name='login'),
    path('logout/', UserLogout.as_view(),  name='logout'),
]