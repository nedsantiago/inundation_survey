from django.urls import path
from . import views

urlpatterns = [
        path('', views.survey_home, name='survey-home'),
        path('about/', views.survey_about, name='survey-about'),
        path('survey/', views.survey_form_view, name='survey-form'),
]