from django.db import models


# Create your models here.
class FizzBuzz(models.Model):
    fizzbuzz_id = models.AutoField(primary_key=True)
    useragent = models.CharField(max_length=255, editable=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)