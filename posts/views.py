from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from .models import Post, Like, Ingredients, Rate
from .forms import PostForm, RateForm
from django.db.models import Count, Avg
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def index(request):
    return render(request, 'posts/index.html')


@login_required(login_url='/posts/')
def post_create(request):
    post_form = PostForm()

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.owner = request.user
            post.save()
            post.ingredients.set(post_form.cleaned_data['ingredients'])
            return HttpResponseRedirect(reverse('posts:post_list'))
    return render(request, 'posts/post_create.html', context={'form': post_form})


def post_list(request):
    posts = Post.objects.annotate(avg_rating=Avg('rate__score'))

    pk = request.GET.get('ingredient', None)
    if pk is not None:
        try:
            if Ingredients.objects.filter(pk=pk).exists():
                ingredient = Ingredients.objects.get(pk=pk)
                posts = posts.filter(id__in=ingredient.posts.values('id'))
            else:
                return HttpResponseRedirect(reverse('posts:post_list'))
        except ValueError:
            return HttpResponseRedirect(reverse('posts:post_list'))

    ingredients = Ingredients.objects.annotate(num_posts=Count('posts')).order_by('-num_posts')[:5]

    return render(request, 'posts/post_list.html', context={'posts': posts, 'ingredients': ingredients})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    rate_form = RateForm()

    if request.user.is_authenticated:
        like = Like.objects.filter(post=post, user=request.user)
        if Rate.objects.filter(post=post, user=request.user).exists():
            rate = Rate.objects.get(post=post, user=request.user)
            rate_form = RateForm(instance=rate)
    else:
        like = None

    return render(request, 'posts/post_detail.html', context={'post': post, 'like': like, 'rate_form': rate_form})


@login_required(login_url='/posts/')
def post_edit(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)

        if post.owner == request.user:
            form = PostForm(data=request.POST, files=request.FILES, instance=post)

            if form.is_valid():
                form.save(commit=True)
                return HttpResponseRedirect(reverse('posts:detail', kwargs={'pk': pk}))

            return render(request, 'posts/post_edit.html', context={'form': form, 'pk': pk})
        else:
            raise PermissionDenied
    else:
        if Post.objects.filter(pk=pk).exists():
            post = Post.objects.get(pk=pk)

            if post.owner == request.user:
                post_form = PostForm(instance=post)
                return render(request, 'posts/post_edit.html', context={'form': post_form, 'pk': pk})
        raise PermissionDenied


@login_required(login_url='/posts/')
def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)

        if post.owner == request.user:
            post.delete()
        else:
            raise PermissionDenied

    return HttpResponseRedirect(reverse('posts:post_list'))


def post_like(request, pk):
    if request.user.is_authenticated and request.method == 'POST':
        post = Post.objects.get(pk=pk)

        if not Like.objects.filter(post=post, user=request.user).exists():
            # user likes the post if he/she hasn't liked it before
            like = Like(post=post, user=request.user)
            like.save()

    return HttpResponseRedirect(reverse('posts:detail', kwargs={'pk': pk}))


def post_unlike(request, pk):
    if request.user.is_authenticated and request.method == 'POST':
        post = Post.objects.get(pk=pk)

        if Like.objects.filter(post=post, user=request.user).exists():
            # user unlikes the post if he/she has liked it before
            like = Like.objects.get(post=post, user=request.user)
            like.delete()

    return HttpResponseRedirect(reverse('posts:detail', kwargs={'pk': pk}))


def post_rate(request, pk):
    if request.user.is_authenticated and request.method == 'POST':
        post = Post.objects.get(pk=pk)

        if Rate.objects.filter(post=post, user=request.user).exists():
            rate = Rate.objects.get(post=post, user=request.user)
            form = RateForm(data=request.POST, instance=rate)

            if form.is_valid():
                form.save(commit=True)
        else:
            form = RateForm(request.POST)
            if form.is_valid():
                rate = form.save(commit=False)
                rate.user = request.user
                rate.post = post
                rate.save()

    return HttpResponseRedirect(reverse('posts:detail', kwargs={'pk': pk}))

