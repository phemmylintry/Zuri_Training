from django.urls import path
from . import views

urlpatterns = [
    path('create-user/', views.UserCreate.as_view(), name='account-create')
]
