import uuid
from django.contrib.auth.models import AbstractUser,BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404


class UserManager(BaseUserManager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

    def create_user(self, username, email, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('User must have an email.')
        
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password, **kwargs):
        """ Create and return a `User` with superuser (admin) permissions."""
        
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
                raise TypeError('Superusers must have anemail.')
        if username is None:
            raise TypeError('Superusers must have an  username.')
        
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user


class User(AbstractUser, PermissionsMixin):

    USER_TYPES = {
        "staff": "staff",
        "customer": "customer",
    }

    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    post_code = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=10, choices=USER_TYPES, default='Select a role')
    is_deleted = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()
    
    def __str__(self):
        return f"{self.email}"
        
    # @property
    # def username(self):
    #     if self.first_name and self.last_login is not None:
    #         return f"{self.first_name} {self.last_name}"
    #     return f"{self.email.split('@')[0]}"

    # def create(self, **obj_data):

    #     if obj_data['first_name'] and obj_data['last_name'] is not None:
    #         obj_data['username'] = f"{(obj_data['first_name'], obj_data['last_name'])}"

    #     obj_data['username'] = obj_data['email'].split('@')[0]
        
    #     return super().create(**obj_data)