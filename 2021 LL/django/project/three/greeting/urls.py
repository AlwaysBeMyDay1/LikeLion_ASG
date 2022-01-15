from django.urls import path
from . import views


urlpatterns = [
    path('result/', views.gt_result, name='greeting'),
]
