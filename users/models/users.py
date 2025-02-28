from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from _base.files import upload_to_kwargs, upload_to_generic
from .users_base import MiFinanzaAbstractBaseUser
from _base.models import BaseModel



class MiFinanzaUsUser(MiFinanzaAbstractBaseUser):
  
    phone = models.CharField(max_length=150, blank=True, null=True)
    photo = models.ImageField(upload_to=upload_to_kwargs(upload_to_generic, subfolder="user_photo"), null=True, blank=True)
    initials = models.CharField(max_length=20, null=True, blank=True)