from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer
from .models import UserProfile

# Create your views here.

# The api view to create a pprofile 
@api_view(["POST"])
def create_profile(request):

    #Gets the data and serializes it 
    serializer=ProfileSerializer(data=request.data)

    #Checks if the serializer is valid and then save it 
    if serializer.is_valid():
        serializer.save()

        # returns a response with the users profile information
        return Response({"userprofile":serializer.data})
    # Returns a 404 error if the request made is bad 
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#Api view to view any profile 
@api_view(['GET'])
def view_profile(request,username):
    #checks if a user profile with tbhe users id exist
    profile=get_object_or_404(UserProfile,user=username)

    #Serializes the profile data
    serializer=ProfileSerializer(instance=profile)
    
    #Returns the data as a response 
    return Response({"userprofile":serializer.data})


# @api_view(["PUT"])
# def update_profile(request,username):
#     #Gets the data and serializes it 
#     serializer=ProfileSerializer(data=request.data)

#     #Checks if the serializer is valid and then save it 
#     if serializer.is_valid():
#         serializer.save()

#         # returns a response with the users profile information
#         return Response({"userprofile":serializer.data})
#     # Returns a 404 error if the request made is bad 
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



