from django.db import models
from users.models import User
# Create your models here.


class Ingredients(models.Model):
    name = models.CharField(max_length=120, blank=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    ingredients = models.ManyToManyField(Ingredients, related_name='posts')

    title = models.CharField(max_length=120, blank=False, verbose_name='Title')
    description = models.TextField(max_length=1200, blank=False, verbose_name='Description')
    image = models.ImageField(upload_to='images/', verbose_name='Image')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'sendings'
        verbose_name_plural = 'sendings'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    RATINGS_CHOICES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    score = models.IntegerField(max_length=1, choices=RATINGS_CHOICES)

    date_rated = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

