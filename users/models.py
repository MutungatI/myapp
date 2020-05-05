from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='noimage.jpg',upload_to='proffile_pics')

    def __str__(self):
        return f'{self.user.username} profile'