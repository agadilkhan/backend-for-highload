from django.contrib import admin
from blog.models import Post

# Customize the Post admin interface
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Fields to display in the list view
    search_fields = ('title',)  # Add search functionality for the 'title' field

# Register the Post model with the customized admin interface
admin.site.register(Post, PostAdmin)