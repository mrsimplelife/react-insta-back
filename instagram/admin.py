from typing import Any
from instagram.models import Comment, Post, Tag
from django.contrib import admin
from django.utils.safestring import mark_safe


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["photo_tag", "caption"]
    list_display_links = ["caption"]

    def photo_tag(self, post):
        return mark_safe(
            f'<img src="{post.photo.url}" style="width: 100px;" alt="{post.caption}"/>'
        )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
