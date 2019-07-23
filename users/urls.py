from django.urls import path
from . import views

app_name = 'users'

urlpatterns=[
    path('register/', view=views.register, name='register'),
    path('login/', view=views.user_login, name='login'),
    path('logout/', view=views.user_logout, name='logout'),
]