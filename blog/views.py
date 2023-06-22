from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from blog.models import Post
from django.views import generic


# CRUD = Create, Retrieve, Update, Delete


# __________________Retrieve____________________

class IndexListView(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=True)
    context_object_name = "posts"
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"


def index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)


def get_post_detail(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk)
    return render(request, "blog/post_detail.html", {"post": post})


# ___________________End Retrieve_________________


# _________________Create_________________________

class PostCreateView(generic.CreateView):
    model = Post
    template_name = "blog/post_create.html"
    fields = ["title", "content", "cover", "status"]
    success_url = reverse_lazy("index-page")


# def create_post(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         content = request.POST.get("content")
#         if title and content:
#             post = Post.objects.create(title=title, content=content)
#             post.save()
#             return reverse_lazy("index-page")
#     return render(request, "blog/post_create.html")
# _________________End Create_____________________

# _________________Delete_________________________

class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("index-page")


# _________________End Delete_____________________

# ________________Update__________________________

class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index-page")

# ________________End Update______________________

# def get_about(request):
#     return render(request, "blog/about.html")


def get_contacts(request):
    return render(request, "blog/contacts.html")


def post_update(request, pk):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title and content:
            post = Post.objects.update(pk=pk, title=title, content=content)

            post.save()
            return reverse_lazy("index-page")

    return render(request, "blog/post_update.html")


def post_delete(request, pk):
    if request.method == "POST":
        post = Post.objects.get(pk=pk)
        post.delete()
    return render(request, "blog/post_delete.html")
