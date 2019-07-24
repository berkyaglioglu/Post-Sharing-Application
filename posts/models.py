from django.db import models
from users.models import User
# Create your models here.


class Post(models.Model):

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=False, verbose_name='Title')
    ingredients = models.TextField(max_length=1200, blank=False, verbose_name='Ingredients')
    description = models.TextField(max_length=1200, blank=False, verbose_name='Description')
    img = models.ImageField(upload_to='images/', verbose_name='Image')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'sendings'
        verbose_name_plural = 'sendings'

