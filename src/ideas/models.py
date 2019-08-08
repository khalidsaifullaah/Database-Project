from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Catagory(models.Model):
    catagory = models.CharField(max_length=30)

    def __str__(self):
        return self.catagory


class Idea(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(blank=True, upload_to='idea_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    catagory = models.ManyToManyField(Catagory)
    area = models.CharField(max_length=30)
    division = models.CharField(blank=True,max_length=30)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('idea-detail', kwargs={'pk': self.pk})


