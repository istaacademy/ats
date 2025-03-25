from django.contrib import admin
from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'created_at', 'is_reply', 'updated_at',)
    search_fields = ('body',)
    raw_id_fields = ("user", 'course', 'reply')
    list_filter = ('created_at', 'updated_at', 'is_reply')



