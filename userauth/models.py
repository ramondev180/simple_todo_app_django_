from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def create_user(self, email, password, **kwargs):
       if email is None:
           raise ValueError('Email must be provided')
       if password is None:
           raise ValueError('Password must be provided')
       user = self.model(email=self.normalize_email(email), **kwargs)
       user.set_password(password)
       user.save(using=self._db)
       return user
    
    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class User(AbstractUser):
    username = None
    email = models.EmailField(blank=True,unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []