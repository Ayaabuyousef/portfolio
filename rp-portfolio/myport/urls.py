from django.urls import path
from myport import views

urlpatterns = [
    path('', views.myport,name='myport'),
]