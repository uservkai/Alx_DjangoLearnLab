from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_photos/')
    
    REQUIRED_FIELDS = ["date_of_birth", "profile_photo"]
    
    def __str__(self):
        return self.username
    
class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        #creates and saves users with the details
        if not email:
            raise ValueError("Users must have and email address")
        
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )
        
        user.set_password(password)
        user.save(using=seld._db)
        return user
    
    def create_superuser(self, email, date_of_bith, password=None):
        user=self.create_user(
            email,
            password=password,
            date_of_birth=date_of_bith,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user