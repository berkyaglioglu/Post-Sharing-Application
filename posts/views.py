from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from .models import Post, Like, Ingredients
from .forms import PostForm
import operator


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
            for choice in post.choices:
                if not Ingredients.objects.filter(name=choice):
                    ingredient = Ingredients(name=choice)
                    ingredient.save()
                post.ingredients.add(Ingredients.objects.get(name=choice))
            return HttpResponseRedirect(reverse('posts:post_list'))
    return render(request, 'posts/post_create.html', context={'form': post_form})


def post_list(request, pk=None):
    if pk is None:
        post_list = Post.objects.all()
    else:
        ingredient = Ingredients.objects.get(pk=pk)
        post_list = ingredient.post_set.all()

    ingredient_counts = {}
    for ingredient in Ingredients.objects.all():
        ingredient_counts[ingredient.name] = ingredient.post_set.count()
    sorted_ingredient_counts = sorted(ingredient_counts.items(), key=operator.itemgetter(1))
    sorted_ingredient_counts.reverse()
    ingredients_list = []
    for ingredient in sorted_ingredient_counts:
        ingredients_list.append(Ingredients.objects.get(name=ingredient[0]))

    return render(request, 'posts/post_list.html', context={'post_list': post_list, 'ingredients': ingredients_list})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user.is_authenticated:
        like = Like.objects.filter(post=post, user=request.user)
    else:
        like = None
    return render(request, 'posts/post_detail.html', context={'post': post, 'like': like})


def post_edit(request, pk):
    if request.user.is_authenticated and request.method == 'POST':
        post = Post.objects.get(pk=pk)
        if post.owner == request.user:
            post_form = PostForm(instance=post)
            return render(request, 'posts/post_edit.html', context={'form': post_form, 'pk': pk})
    return HttpResponseRedirect(reverse('posts:detail', kwargs={'pk': pk}))


def update(request, pk):
    if request.user.is_authenticated and request.method == 'POST':
        post = Post.objects.get(pk=pk)

        if post.owner == request.user:
            form = PostForm(data=request.POST, instance=post)

            if form.is_valid():
                post_updated = form.save(commit=True)
                post_updated.ingredients.clear()

                for choice in post_updated.choices:
                    if not Ingredients.objects.filter(name=choice):
                        ingredient = Ingredients(name=choice)
                        ingredient.save()
                    post.ingredients.add(Ingredients.objects.get(name=choice))

                return HttpResponseRedirect(reverse('posts:detail', kwargs={'pk': pk}))

            return render(request, 'posts/post_edit.html', context={'form': form, 'pk': pk})

    return HttpResponseRedirect(reverse('posts:detail', kwargs={'pk': pk}))


def delete(request, pk):
    if request.user.is_authenticated and request.method == 'POST':
        post = Post.objects.get(pk=pk)

        if post.owner == request.user:
            post.delete()

    return HttpResponseRedirect(reverse('posts:post_list'))


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

