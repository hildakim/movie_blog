from django.db import models

# Create your models here.

class Blog(models.Model):
    review_title = models.CharField(max_length=200)
    movie = models.CharField(max_length=100, null=True)
    nickname = models.CharField(max_length=100)
    upload_date = models.DateTimeField()
    review_body = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True, blank=True)

    def __str__(self):
        return self.review_title 

    def summary(self):
        return self.review_body[:100]+'...'
