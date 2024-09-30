from django.db import models
from django.utils import timezone

from source_base.core.middleware.user import get_current_user


class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.UUIDField(max_length=16, null=True, blank=True)
    created_by = models.UUIDField(max_length=16, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.created_by = user.id
        super(BaseModel, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.updated_at = timezone.now()
            self.updated_by = user.id
        super(BaseModel, self).save(*args, **kwargs)