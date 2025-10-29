from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment
from taggit.forms import TagField, TagWidget

#registration form for new users
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", 'email', 'password1', 'password2')

#profile update form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture')

#email update form for profile view        
class UserEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
        
#form for creating and updating blog posts
class PostForm(forms.ModelForm):
    tags = TagField(
        required=False,
        help_text="Enter tags separated by commas.",
        widget=TagWidget(),
    )
    
    class Meta:
        model = Post
        fields = ('title', 'content', 'tags') #author,tag and published_date are set automatically
        
    def clean_title(self):
            title = self.cleaned_data.get('title')
            if not title or len(title) < 5:
                raise forms.ValidationError("Title must be at least 5 characters long.")
            return title
        
    def clean_content(self):
            content = self.cleaned_data.get('content')
            if not content or len(content) < 10:
                raise forms.ValidationError("Content must be at least 10 characters long.")
            return content
        
#form for adding comments to blog posts
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content or len(content) < 3:
            raise forms.ValidationError("Comment must be at least 3 characters long.")
        return content