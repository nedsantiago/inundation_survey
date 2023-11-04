from django.urls import path
from . import views

urlpatterns = [
        path('backend/', views.hello_world, name='hello_world'),
]