from django.contrib.auth.views import LoginView, LogoutView #import built-in auth views
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView, PostByTagListView, SearchResultsView
from blog import views as blog_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html', redirect_authenticated_user=True ), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name = 'logout'),
    path('register/', blog_views.register, name='register'), #register view
    path('profile/', views.profile, name='profile'), #profile view
    #path search search post via query parameter
    path('posts/', PostListView.as_view(), name='post-list'), #path post list shows all blog posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), #path post update updates existing blog post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), #path post delete deletes existing blog post
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view, name='add-comment'), #path add comment to blog post
    path('comment/<int:pk>/update/', CommentUpdateView.as_view, name='edit-comment'), #path edit comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view, name='delete-comment'), # path delete comment
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'), #path posts by tag
    path('search/', SearchResultsView.as_view(), name='search-results'), #path search
]
