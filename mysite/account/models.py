from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    nickname = models.CharField(max_length = 255, null=True, unique=True)
    school = models.TextField(blank=True, null=True)
    git_address = models.TextField(blank=True,null=True)
    adopted_answer = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="account/profile/", blank=True, null=True)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
