from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from time import time


def card_image_filename(instance):
    timestamp = int(time())
    return 'cards/%s%d.jpg' % (instance, timestamp)


@python_2_unicode_compatible
class Card(models.Model):
    title = models.CharField(max_length=140, unique=True)
    is_title_visible = models.BooleanField(default=True)
    text = models.TextField()
    secondary_text = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to=card_image_filename, null=True, blank=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_created_by')
    updated_by = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_updated_by')

    def __str__(self):
        return self.title
