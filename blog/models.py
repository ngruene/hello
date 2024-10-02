from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # using charfields instead of datetime because of formatting issues
    edit_date = models.DateTimeField(null=True, blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    draft = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        Post.draft = False 
        self.save()

    def __str__(self):
        return self.title