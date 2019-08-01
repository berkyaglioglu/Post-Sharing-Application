from django.urls import path
from . import views

app_name = 'posts'

urlpatterns=[
    path('', view=views.post_list, name='post_list'),
    path('create/', view=views.post_create, name='post_create'),
    path('<int:pk>/', view=views.post_detail, name='detail'),
    path('<int:pk>/edit/', view=views.post_edit, name='edit'),
    path('<int:pk>/delete/', view=views.post_delete, name='delete'),
    path('<int:pk>/like/', view=views.post_like, name='like'),
    path('<int:pk>/unlike/', view=views.post_unlike, name='unlike'),
    path('<int:pk>/rate/', view=views.post_rate, name='rate'),
]
