from django.urls import path
from . import views

app_name = 'posts'

urlpatterns=[
    path('', view=views.post_list, name='post_list'),
    path('create/', view=views.post_create, name='post_create'),
    path('<int:pk>/', view=views.post_detail, name='detail'),
    path('<int:pk>/edit/', view=views.post_edit, name='edit'),
    path('<int:pk>/delete/', view=views.post_delete, name='delete'),
    path('<int:pk>/update/', view=views.handle_update, name='update'),
    path('<int:pk>/like/', view=views.handle_like, name='like'),
    path('<int:pk>/unlike/', view=views.handle_unlike, name='unlike'),
    path('<int:pk>/rate/', view=views.handle_rate, name='rate'),
]
