from django.urls import path
from blogs import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("about/", views.get_about, name="about-page"),
    path("contacts/", views.get_contacts, name="contacts-page"),
]
