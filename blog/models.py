from django.db import models

# Create your models here.

class Blog(models.Model):
    diary_title = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100)
    upload_date = models.DateTimeField()
    diary_body = models.TextField()

    def __str__(self):
        return self.diary_title 

    def summary(self):
        return self.diary_body[:100]+'...'
