from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post

admin.site.site_header = 'MyBlog'
admin.site.site_title = 'Admin'

class PostAdmin(admin.ModelAdmin):
     list_display = ('title', 'author', 'date')
     list_filter = ('author', 'date')


admin.site.register(Post, PostAdmin)
admin.site.unregister(Group)


