from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_images/')
    
class GymInfo(models.Model):
    gym_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField()
    website = models.TextField()
    
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class GalleryItem(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=100)
    description = models.TextField()
    
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='trainer_images/')
    description = models.TextField()
    
    
    
    
