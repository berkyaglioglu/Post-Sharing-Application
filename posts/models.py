from django.db import models
from users.models import User
# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')

    title = models.CharField(max_length=120, blank=False, verbose_name='Title')
    ingredients = models.TextField(max_length=1200, blank=False, verbose_name='Ingredients')
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


