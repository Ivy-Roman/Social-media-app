from django.db import models
from django.contrib.auth.models import User as auth_user, PermissionsMixin

# Create your models here.
class User(auth_user, PermissionsMixin):
    
    def __str__(self):
        return f"@{self.username}"
