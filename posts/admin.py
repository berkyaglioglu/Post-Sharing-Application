from django.contrib import admin
import django
from .models import Post, Ingredients

admin.site.register(Post)
admin.site.register(Ingredients)
