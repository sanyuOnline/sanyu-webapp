
from django.contrib import messages
from .models import BlogPost
from django.views.generic import ListView, DetailView
# Create your views here.

class BlogList(ListView):
    model = BlogPost
    template_name = 'pages/blog_list.html'
    context_object_name = 'blogs'

class BlogDetail(DetailView):
    model = BlogPost
    template_name = 'pages/blog_detail.html'
    context_object_name = 'blog'
    
"""
    def get_context_data(self, *args, **kwargs):
        context = super(Pdt_detail, self).get_context_data( **kwargs)
        context['products'] = Product.objects.all().order_by('?')[:4]
        context['productss'] = Product.objects.all().order_by('?')[:9]
        context['pdts'] = Product.objects.all().order_by('?')[:3]
        return context

"""