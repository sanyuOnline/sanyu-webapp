from django.db import models
from users.models import CustomUser
from django.urls import reverse

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField( max_length=50)
    small_image = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    large_image = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    text = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Blogpost_detail", kwargs={"pk": self.pk})

