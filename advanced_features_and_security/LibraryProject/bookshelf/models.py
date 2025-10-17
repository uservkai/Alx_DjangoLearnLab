from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"Book : {self.title} by {self.author} ({self.publication_year})"

    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        #creates and saves users with the details
        if not email:
            raise ValueError("Users must have and email address")
        
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, date_of_birth, password=None):
        user=self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_photos/')
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["date_of_birth"]
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.username    