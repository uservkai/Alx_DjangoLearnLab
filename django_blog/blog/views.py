from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ProfileForm, UserEmailForm, PostForm, CommentForm
from django.contrib import messages # import messages framework
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404

# Create your views here.
def register(request): # registration of new user
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required #ensure only logged-in users can access
def profile_view(request):
    user = request.user
    profile = user.profile
    
    if request.method == 'POST':
        email_form = UserEmailForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        
        if email_form.is_valid() and profile_form.is_valid():
            email_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile') # redirect to avoid resubmission
    else:
        email_form = UserEmailForm(instance=user)
        profile_form = ProfileForm(instance=profile)
        
    return render(request, 'blog/profile.html', {
        'user_form': email_form,
        'profile_form': profile_form
    })
    
#implementing crud operations for blog posts
#List all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    
#View details of a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

#Create a new blog post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#Update an existing blog post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
#Delete a blog post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

#setting up functon based views
@login_required
def add_comment(request, post_id):   #adding comments to blog posts
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added successfully!")
            return redirect('post-detail', pk=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})

#editing a comment
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk = comment_id)
    if request.user != comment.author:
        messages.error(request, "You are not authorized to edit this comment.")
        return redirect('post-detail', pk=comment.post.pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully!")
            return redirect('post-detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})

#deleting a comment
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, "You are not authorized to delete this comment.")
        return redirect('post-detail', pk=comment.post.pk)
    
    if request.method == 'POST':
        post_pk = comment.post.pk
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
        return redirect('post-detail', pk=post_pk)
    
    return render(request, 'blog/delete_comment.html', {'comment': comment})
