from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('privacypolices/', views.privacypolices, name="privacypolices"),
    path('contactus/', views.contactus, name="contactus"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('<str:slug>/', views.post, name="post"),
]
