from django.db import models

# Create your models here.

class Quote(models.Model):
    quote = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=256)
    quote_len = models.IntegerField()


    def __str__(self):
        return f"{self.author}:{self.quote}"