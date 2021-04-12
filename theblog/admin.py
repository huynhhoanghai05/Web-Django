from django.contrib import admin
from .models import Post, Category, Profile, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']



admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
