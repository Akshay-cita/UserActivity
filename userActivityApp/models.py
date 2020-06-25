from django.db import models
from django.utils import timezone
import pytz

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50,null=True)
    reg_id=models.CharField(max_length=9,null=True)
    tz=models.CharField(max_length=100,null=True)



    def __str__(self):
        return self.name

class ActivityPeriod(models.Model):
     name=models.ForeignKey(User,related_name='activity_periods',on_delete=models.CASCADE)
     StartTime=models.DateTimeField(editable=True,null=True)
     EndTime=models.DateTimeField(editable=True,null=True)
     
