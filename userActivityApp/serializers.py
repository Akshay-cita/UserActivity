from rest_framework.serializers import ModelSerializer
from .models import User,ActivityPeriod
from BackendTest import settings
import pytz
import datetime

class ActivityPeriodSerializer(ModelSerializer):
    def to_representation(self, instance):
        representation = super(ActivityPeriodSerializer, self).to_representation(instance)
        representation['StartTime'] = instance.StartTime.strftime('%B %d %Y %I:%M %p')
        representation['EndTime'] = instance.EndTime.strftime('%B %d %Y %I:%M %p')
        return representation
    class Meta:
        model=ActivityPeriod
        fields=('StartTime','EndTime')



class UserSerializer(ModelSerializer):
    activity_periods=ActivityPeriodSerializer(many=True,read_only=True)
    class Meta:

        model=User
        fields=('reg_id','name','tz','activity_periods')
