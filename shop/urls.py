from django.urls import path
from shop import views

urlpatterns = [
    path("", views.index, name='home'),
    path("contact", views.contact, name='contact'),

]

