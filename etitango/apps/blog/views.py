from django.shortcuts import render
from django.contrib.auth.views import TemplateView

# UTILS
from utils.defs import ReviewContextMixin

class BlogView(ReviewContextMixin, TemplateView):
    template_name = 'blog.html'
