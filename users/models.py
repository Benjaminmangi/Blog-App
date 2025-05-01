from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('author', 'Author'),
        ('user', 'Regular User'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return self.username
    
    def is_admin(self):
        return self.role == 'admin'
    
    def is_author(self):
        return self.role == 'author'
    
    def is_regular_user(self):
        return self.role == 'user' 