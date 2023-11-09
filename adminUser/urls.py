from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('tests', views.tests, name="tests"),
    path('tests/<slug:slug>', views.test, name="test"),
    path('tests/<slug:slug>/generate-result', views.generateResult, name="generate"),
]