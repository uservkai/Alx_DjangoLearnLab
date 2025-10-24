from django.contrib.auth.views import LoginView, LogoutView #import built-in auth views
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    path('register/', views.register, name='register'), #register view
    path('profile/', views.profile_view, name='profile'), #profile view
    #path search search post via query parameter
    path('posts/', PostListView.as_view(), name='post-list'), #path post list shows all blog posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), #path post update updates existing blog post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), #path post delete deletes existing blog post
    path('post/<int:pk>/comments/new', CommentCreateView.as_view, name='add-comment'), #path add comment to blog post
    path('comments/<int:pk>/update/', CommentUpdateView.as_view, name='edit-comment'), #path edit comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view, name='delete-comment'), # path delete comment
    
]
