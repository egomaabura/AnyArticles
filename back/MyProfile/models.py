from django.db import models
from django_boost.models.mixins import LogicalDeletionMixin, UUIDModelMixin, TimeStampModelMixin
import uuid

#####
## ユーザー
#####
class User(LogicalDeletionMixin, UUIDModelMixin, TimeStampModelMixin):
    name = models.CharField(max_length=30, null=False)
    icon = models.ImageField(null=True, blank=True)
    mail = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
    profile = models.TextField(null=True, blank=True)
