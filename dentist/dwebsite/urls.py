from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
    path('doctors/', views.doctors, name="doctors"),
    path('blog/', views.blog, name="blog"),
]
