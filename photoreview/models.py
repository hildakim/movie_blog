from django.db import models
from django import forms

# Create your models here.


def minmax_value_0_5_validator(value):
	if value > 5 or value < 0:
		raise forms.ValidationError('0~5의 값을 선택해야합니다.')


class PhotoReview(models.Model):
  review_title = models.CharField(max_length=200)
  movie = models.CharField(max_length=100, null=True)
  rating = models.IntegerField(null=True, blank=True, default=3, validators=[minmax_value_0_5_validator])
  upload_date = models.DateTimeField()
  image = models.ImageField(upload_to='photoreview/', null=True, blank=True)

  def __str__(self):
    return self.review_title 