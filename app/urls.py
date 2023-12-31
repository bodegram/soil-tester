from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('auth', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('register', views.register, name="register"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('settings', views.settings, name="settings"),
    path('profile', views.profile, name="profile"),
    path('change-password', views.changePassword, name="changePassword"),
    path('update-profile', views.updateProfile, name="updateProfile"),
    path('change-username', views.changeUsername, name="changeUsername"),
    path('change-email', views.changeEmail, name="change-email"),
    path('reset-password', views.resetPassword, name="resetPassword"),
    path('test', views.test, name="test"),
    path('test/create', views.createTest, name="createTest"),
    path('tests', views.allTests, name="allTests"),
    path('tests/<int:id>', views.viewTest, name="viewTest"),
    path('result/<slug:slug>', views.pdfResult, name="pdf_result"),
    
    
]