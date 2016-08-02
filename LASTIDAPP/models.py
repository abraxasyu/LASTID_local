from django.db import models

# Create your models here.
class nextid(models.Model):
    nextid_id=models.CharField(max_length=200)
    nextid_time=models.DateTimeField(auto_now_add=True)