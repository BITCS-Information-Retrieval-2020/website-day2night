from django.contrib import admin

# Register your models here.
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_time']
    fields = ['name', 'email', 'url', 'text', 'post']

    # def save_model(self, request, obj, form, change):
    #     obj.author = request.user
    #     super().save_model(request, obj, form, change)

admin.site.register(Comment, CommentAdmin)
