from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Diagnosis(models.Model):
    image = models.ImageField(upload_to='images/')
    dateOfSubmission = models.DateTimeField(auto_now_add=True)
    diagnosis = models.TextField(max_length=200,default="None")
    confidence = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)
    class Meta:
        ordering=['-dateOfSubmission']