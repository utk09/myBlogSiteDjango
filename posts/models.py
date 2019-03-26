from django.db import models
from datetime import datetime

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # image = models.ImageField()
    created_at = models.DateTimeField(
        default=datetime.now, blank=True, null=True)
    def __str__(self):
        return self.title
# blank --> for models, null --> for database, required --> for forms
# this makes sure that user puts in the DateTimeField

    class Meta:
        # this makes sure that we don't have default plural values
        verbose_name_plural = 'Posts'
