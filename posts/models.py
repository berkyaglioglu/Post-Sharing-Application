from django.db import models
from users.models import User
from multiselectfield import MultiSelectField
# Create your models here.


class Ingredients(models.Model):
    name = models.CharField(max_length=120, blank=False)


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    INGREDIENT_CHOICES = (
        ('tomato', 'Tomato'),
        ('eggplant', 'Eggplant'),
        ('celery', 'Celery'),
        ('egg', 'Egg'),
        ('milk', 'Milk'),
        ('fish', 'Fish'),
        ('chicken', 'Chicken'),
        ('oil', 'Oil')
    )
    # picked_ingredients
    ingredients = models.ManyToManyField(Ingredients)
    choices = MultiSelectField(choices=INGREDIENT_CHOICES, max_length=1000, blank=True)

    rating = models.FloatField(max_length=10, default=0)
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

    RATINGS = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    rating = models.IntegerField(max_length=1, choices=RATINGS, default=5)

    date_rated = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

