from django.urls import path
from profiles_api import views


urlpatterns = [
    path('', views.HelloAPIView.as_view(), name='hello'),
]