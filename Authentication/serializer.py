from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Jobs

#  user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ( 'id','username', 'email', 'password')


#  Jobs serializer 
class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs  # Specify the model associated with the serializer
        fields = '__all__'


class ResetPasswordEmailSerializer(serializers.Serializer):
    email=serializers.EmailField(min_length=2)

    class Meta:
        fields=["email"]


class PasswordResetConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)
    confirm_password = serializers.CharField(max_length=128)

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match")

        return data