from django.db import models

# Create your models here.
import uuid

class AddToDatabase(models.Model):
    user_input = models.CharField(max_length=50, unique=True)
    random_url = models.UUIDField(default=uuid.uuid4)