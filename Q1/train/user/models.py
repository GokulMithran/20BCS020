from django.db import models

# Create your models here.
from django.db import models

class train(models.Model):
   companyName = models.CharField(max_length=20)
   ownerName= models.CharField(max_length=20)
   rollno = models.CharField(max_length=10)
   ownerEmail= models.EmailField(max_length=30)
   accessCode= models.CharField(max_length=20)
   