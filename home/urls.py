from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header="PlacementPiolet admin"
admin.site.site_title="PlacementPiolet admin portal"
admin.site.index_title="Welcome to the PlacementPiolet"

urlpatterns = [
    path("", views.home, name='home'),
    path("assesment", views.assesment, name='assesment'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("instructions", views.instructions, name='instructions'),
    path("test", views.test, name='test'),
    path("test_4", views.test_4, name='test_4'),
    path("login", views.loginpage, name='login'),
    path("signup", views.signup, name='signup'),
    # path("session_man", views.session_man, name='session_man'),

]