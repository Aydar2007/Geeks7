from django import forms
from blog.models import Comment
from blog.models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "comment"]


