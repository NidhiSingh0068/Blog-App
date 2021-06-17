from django.views import generic
from .models import Post
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)

    return render(request, template_name, context= {'post': post})

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        content =request.POST['content']
        contact=Contact(name=name, email=email, content=content)
        contact.save()
    return render(request, "contact.html")





def search(request):
    query=request.GET['query']
    allPosts= Post.objects.filter(title__icontains=query)
    params={'allPosts': allPosts}
    return render(request, 'search.html', params)
