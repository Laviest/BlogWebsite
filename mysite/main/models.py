from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_search", null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    blog_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):

        return self.title
