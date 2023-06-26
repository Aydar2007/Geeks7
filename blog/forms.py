from django import forms
from blog.models import Comment
from blog.models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "comment"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
