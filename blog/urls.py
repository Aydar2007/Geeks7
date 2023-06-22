from django.urls import path
from django.views.generic import TemplateView

from blog import views

urlpatterns = [
    path("", views.IndexListView.as_view(), name="index-page"),
    path("about/", TemplateView.as_view(template_name="blog/about.html"), name="about-page"),
    path("contacts/", views.get_contacts, name="contacts-page"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post-detail"),
    path("post/update/<int:pk>", views.PostUpdateView.as_view(), name="post-update"),
    path("post/delete/<int:pk>", views.PostDeleteView.as_view(), name="post-delete"),
    path("post/create", views.PostCreateView.as_view(), name="post-create"),
]