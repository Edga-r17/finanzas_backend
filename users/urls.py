from django.urls import path, include
from users.views import *

urlpatterns = [
    path('auth/', UserProfileView.as_view(), name='UserProfileView'),
]