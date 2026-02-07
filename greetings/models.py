from django.db import models

class Greeting(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    viewed = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    last_viewed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
