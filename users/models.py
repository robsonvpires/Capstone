from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='detault.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    #overwrite the save method
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        #checks if the image is greater than 300x300, if so it will be redimentioned 
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
