from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from post.models import Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = (
        'id',
        'title',
    )
