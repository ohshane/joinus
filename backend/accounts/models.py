import uuid

from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    account_id = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
