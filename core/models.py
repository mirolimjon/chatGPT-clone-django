from django.db import models
from accounts.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} -  {self.message[:20]}"