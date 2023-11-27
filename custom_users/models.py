from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404
import uuid



from core.abstract.models import AbstractModel, AbstractManager

# Create your models here.

class UserManager(BaseUserManager, AbstractManager):
    # def get_object_by_public_id(self, public_id):
    #     try:
    #         instance = self.get(public_id=public_id)

    #         return instance
    #     except (ObjectDoesNotExist, ValueError, TypeError):
    #         return Http404
    
    def create_user(self, username, email, password=None, **kwargs):
        """
        Create and return a `User` with an email, phone number, username and password.
        """
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('User must have an password.')
        

        first_name = kwargs.pop('first_name', '')
        last_name = kwargs.pop('last_name', '')

        user = self.model(
            username=username, 
            email=self.normalize_email(email), 
            first_name=first_name,
            last_name=last_name,
            **kwargs)
        
        user.set_password(password)
        user.save(using=self._db)

        return user
    

    def create_superuser(self, username, email, password, **kwargs):
        """"
            Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        if email is None:
            raise TypeError('Superusers must have an email.')

        if username is None:
            raise TypeError('Superusers must have an username.')


        user = self.create_user(
            username, 
            email, 
            password, 
            # firt_name=kwargs.get('first_name', ''),
            # last_name=kwargs.get('last_name', ''),
            **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)

        return user
    


class User(AbstractModel ,AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    post_liked = models.ManyToManyField("core_post.Post", related_name="liked_by")
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(max_length=500, null=True)
    avatar = models.ImageField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    def like(self, post):
        """Like `post` if it hasn't been done yet"""
        return self.post_liked.add(post)
    
    def remove_like(self, post):
        """Remove a like from a `post`"""
        return self.post_liked.remove(post)
    
    def has_liked(self, post):
        """Return True if the user liked a `post`; else False"""
        return self.post_liked.filter(pk=post.pk).exists()