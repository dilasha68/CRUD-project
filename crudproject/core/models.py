from django.db import models

class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    content = models.TextField()
    date_of_post = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
