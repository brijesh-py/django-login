from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class User(AbstractUser):
    # Your custom fields and methods here
    groups = models.ManyToManyField(
        Group,
        related_name='blog_users',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    class Meta:
        swappable = 'AUTH_USER_MODEL'
