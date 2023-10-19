from authentication.views import login_user, register_user
from django.urls import path

app_name = 'authentication'
urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
]