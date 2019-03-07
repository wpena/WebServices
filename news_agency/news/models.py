from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
import uuid

# Create your models here.


class Author(models.Model):
    author_name = models.CharField(max_length=64)
    user = models.OneToOneField(User, related_name='User',
                             null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.author_name


class Story(models.Model):
    key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    headline = models.CharField(max_length=64)

    story_cat_types = [('pol', 'pol'), ('art', 'art'),
                       ('tech', 'tech'), ('trivia', 'trivia')]
    story_cat = models.CharField(
        max_length=6, choices=story_cat_types)

    story_region_types = [('uk', 'uk'), ('eu', 'eu'),
                          ('w', 'w')]
    story_region = models.CharField(
        max_length=250, choices=story_region_types)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    story_date = models.DateTimeField(auto_now_add=True)
    story_details = models.TextField(max_length=512)

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name_plural = "Stories"
        
    def get_absolute_url(self):
        return reverse('story-detail', kwargs={'pk': self.pk})
