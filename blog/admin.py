from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ["title", "created", "status"]
    list_editable = ["status"]
    list_filter = ["status"]