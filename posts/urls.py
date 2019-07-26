from django.urls import path
from . import views

app_name = 'posts'

urlpatterns=[
    path('', view=views.post_list, name='post_list'),
    path('create/', view=views.post_create, name='post_create'),
    path('<int:pk>/', view=views.post_detail, name='detail'),
    path('like/<int:pk>/', view=views.handle_like, name='like'),
    path('unlike/<int:pk>/', view=views.handle_unlike, name='unlike'),
]
