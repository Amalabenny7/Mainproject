from rest_framework import serializers
from job.models import JobId,Application


class android_seriliser(serializers.ModelSerializer):
    class Meta:
        model=JobId
        fields='__all__'


class android_seriliser1(serializers.ModelSerializer):
    job=serializers.CharField(source='job.jobtitle')
    class Meta:
        model=Application
        fields=['application_id','job','user','status','date','time']
