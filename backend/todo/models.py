from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=80)
    body = models.CharField(max_length=300)
    realized = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]