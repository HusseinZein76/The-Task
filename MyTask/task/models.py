import uuid
from django.db import models

# Create your models here.

class URL(models.Model):
    Owner = models.CharField(max_length=100)
    LongUrl = models.CharField(max_length=1000)
    ShortUrl = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now_add=True)    