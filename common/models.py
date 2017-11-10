from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    deleted_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True
