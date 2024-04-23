from django.db import models
from django.contrib.auth.models import AbstractUser, Group,Permission
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
import uuid
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    # Define your custom fields and methods here
    ADMIN = models.BooleanField('Is Admin',default=False)
    STUDENT = models.BooleanField('Is Student',default=False)
    MANAGER = models.BooleanField('Is Manager',default=False)

    groups = models.ManyToManyField(
        Group,
        through='GroupUser',
        related_name='pages_users_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        through='UserPermission',
        related_name='pages_users_permissions'
    )

    class Meta:
        # Add this Meta class to avoid conflicts with the default 'auth' app
        app_label = 'pages'

# Example through models for the groups field
class GroupUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

# Example through models for the user_permissions field
class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

#User = get_user_model()
# Create your models here.


class createclub(models.Model):
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')  
    profileimg2 = models.ImageField(upload_to='profile_images2', default='blank-profile-picture.png')
    clubname =models.CharField(max_length=100)
    headline = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    clubmanager =models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_clubs')
    clubvicemanager = models.CharField(max_length=100)
    phonenumber1 = models.IntegerField()
    phonenumber2 = models.IntegerField()
    email = models.EmailField()
    category = models.CharField(max_length=100, choices=[('sport', 'Sport'), ('gaming', 'Gaming'), ('technology', 'Technology'), ('society', 'Society'), ('programming', 'Programming'), ('art', 'Art')])
    clubvision = models.TextField()
    clubdescription = models.TextField()

    def _str_(self):
        return self.clubname.username

class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    clubname=models.CharField(max_length=100)
    eventtitle=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post_images')
    postdescription=models.TextField()
    created_at=models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.eventtitle
    
class EventActivity(models.Model):
    clubmanager= models.CharField(max_length=100)
    clubvicemanager = models.CharField(max_length=100)
    clubname = models.CharField(max_length=100)
    email = models.EmailField()
    eventtitle = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    event_image = models.ImageField(upload_to='event_images')  
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.eventtitle  # Return a meaningful representation of the event title
