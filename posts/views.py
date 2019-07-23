from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from .models import Post
from .forms import PostForm


def index(request):
    return render(request, 'posts/index.html')


def post_create(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('posts:post_list'))

    post_form = PostForm()

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save(commit=True)
            return HttpResponseRedirect(reverse('posts:post_list'))
    return render(request, 'posts/post_create.html', context={'form': post_form})


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'posts/post_list.html', context={'post_list': post_list})
