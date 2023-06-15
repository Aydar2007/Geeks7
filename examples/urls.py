from django.urls import path
from examples import views

urlpatterns = [
    # path("", views.index, name="index-page"),
    path("test-template/", views.get_template, name="test-template"),
]
