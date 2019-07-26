from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from .models import Post, Like
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
            post.owner = request.user
            post.save()
            return HttpResponseRedirect(reverse('posts:post_list'))
    return render(request, 'posts/post_create.html', context={'form': post_form})


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'posts/post_list.html', context={'post_list': post_list})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    like = Like.objects.filter(post=post, user=request.user)
    return render(request, 'posts/post_detail.html', context={'post': post, 'like': like})


def handle_like(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=pk)

        if request.method == 'POST':
            if not Like.objects.filter(post=post, user=request.user):
                # user likes the post if he/she hasn't liked it before
                like = Like(post=post, user=request.user)
                like.save()

    return HttpResponseRedirect(reverse('posts:detail', kwargs={'pk': pk}))


def handle_unlike(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=pk)

        if request.method == 'POST':
            if Like.objects.filter(post=post, user=request.user):
                # user unlikes the post if he/she has liked it before
                like = Like.objects.get(post=post, user=request.user)
                like.delete()

    return HttpResponseRedirect(reverse('posts:detail', kwargs={'pk': pk}))

