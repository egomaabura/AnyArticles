from django.db import models
from django_boost.models.mixins import LogicalDeletionMixin
import uuid

#####
## ユーザー
#####
class User(LogicalDeletionMixin):
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True, null=False)
    name = models.CharField(max_length=30, null=False)
    icon = models.ImageField(null=True)
    mail = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
    profile = models.TextField(null=True)
    
    # 登録・更新日時
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
