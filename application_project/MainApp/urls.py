from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user/',  UserView.as_view(), name='user'),
    path('logout/', logout_user, name='logout')
]