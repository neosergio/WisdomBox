from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Card(models.Model):
    text = models.TextField()
    secondary_text = models.TextField(null=True, blank=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank=True)
