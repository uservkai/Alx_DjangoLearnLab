from django.urls import path
from . import views
from .views import list_books, register, SignUpView,admin_view, librarian_view, member_view 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', views.admin_view, name = 'admin_view'),
    path('librarian/', views.librarian_view, name = 'librarian_view'),
    path('member/', views.member_view, name = 'member_view'),
    path('list_books/', views.list_books, name = 'list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name = 'library_detail'),
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name = "logout"),
    path('register/', SignUpView.as_view(), name= 'register'),
    
]
