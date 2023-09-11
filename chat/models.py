from django.conf import settings
from django.db import models
from django.utils import timezone

from django.forms import DateField

# Create your models here.

class Chat(models.Model):
    created_at = models.DateTimeField(default = timezone.now)

class Message(models.Model) :
    text = models.CharField(max_length = 500)
    created_at = models.DateTimeField(default = timezone.now)
   # chat =
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set', default=None , blank=True , null=True) #default=None , blank=True , null=True wichtig!1
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')