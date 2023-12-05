from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Jobs


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ( 'id','username', 'email', 'password')


class JobsSerializer(serializers.ModelSerializer):
    class Meta(object):
        model:Jobs
        fields=('jobtitle','location','company','companylogo','date')