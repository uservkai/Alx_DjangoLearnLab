from django.contrib.auth.views import LoginView, LogoutView #import built-in auth views
from django.urls import path
from . import views


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    path('register/', views.register, name='register'), #register view
    path('profile/', views.profile_view, name='profile'), #profile view
    #path search search post via query parameter
    #path post list lists all blog posts
    #path post detail shows individual blog post details
    #path post create creates new blog post
    #path post update updates existing blog post**
    #path post delete deletes existing blog post**
]
