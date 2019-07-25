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
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse('posts:post_list'))
    return render(request, 'posts/post_create.html', context={'form': post_form})


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'posts/post_list.html', context={'post_list': post_list})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    if request.user.is_authenticated:
        return render(request, 'posts/detail_user.html', context={'post': post, 'user': request.user})
    return render(request, 'posts/detail_anonymous.html', context={'post': post})


def handle_like(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return render(request, 'posts/detail_user.html', context={'post': post, 'user': request.user})


