from django.urls import path
from . import views

urlpatterns = [
    path('wc/', views.wc_home, name='wordcount'),
    path('wc/result', views.wc_result, name='wordlist')
]
