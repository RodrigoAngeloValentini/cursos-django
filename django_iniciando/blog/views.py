from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Category, Post

# Create your views here.
def home(request):

    name = "Rodrigo"
    #categories = ['PHP', 'Java', 'Ruby']
    #for category in categories:
        #Category.objects.create(name=category)

    all_categories = Category.objects.all()

    category_python = Category.objects.get(name='PHP')
    post = Post.objects.filter(status="Published")

    # post = Post()
    # post.name = "Show Post 2"
    # post.content = "Content"
    # post.status = "Published"
    # post.category = category_python
    # post.save()

    context = {
        'name':name,
        'categories':all_categories,
        'posts':post
    }

    return render(request,'blog/home.html', context)

def show_posts_by_category(request, category_id):
    all_categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    posts = Post.objects.filter(category=category, status='Published')

    context = {
        'posts': posts,
        'categories': all_categories,
        'category': category
    }

    return render(request, 'blog/home.html', context)