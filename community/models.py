from django.db import models
from django.contrib.auth.models import User

class SuccessPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='success_posts')
    content = models.TextField()
    image = models.ImageField(upload_to='success_posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d')}"
