import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class URL(models.Model):
    owner = models.ForeignKey(
        User,on_delete=models.CASCADE,null=True,blank=True
    )
    LongUrl = models.CharField(max_length=1000)
    ShortUrl = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now_add=True)    