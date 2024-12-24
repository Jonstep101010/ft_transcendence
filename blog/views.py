from django.shortcuts import render
from blog.models import Post

# Create your views here.
# posts = [
#     {
#         'author': 'Mohamed',
#         'title' : 'My first django blog',
#         'content' : 'random comments',
#         'date_posted': 'Dezember 15, 2024'
#     },
#     {
#         'author': 'Mohamed',
#         'title' : 'My first django blog',
#         'content' : 'random comments',
#         'date_posted': 'Dezember 15, 2024'
#     }
# ]

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'about'})