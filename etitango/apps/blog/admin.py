from django.contrib import admin
from .models import Blog

#Doesn't change anything. For future implementation
class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)
