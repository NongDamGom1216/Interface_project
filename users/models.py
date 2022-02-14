from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(blank=True)
    phone = models.CharField(max_length=64, blank=True)
    Mobile = models.CharField(max_length=64, blank=True)
    address = models.CharField(max_length=64, blank=True)
    Git_url = models.CharField(max_length=64, blank=True)
    Twit_url = models.CharField(max_length=64, blank=True)
    Ins_url= models.CharField(max_length=64, blank=True)
    face_url = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username

def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user)

# 회원 가입 시 Profile 자동 생성
post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)