from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import JobSerializer
from .models import Jobs

# Create your views here.


#Api view to get all jobs
@api_view(['GET'])
def view_jobs(request):

    jobs=Jobs.objects.all()

    #Serializes the job data
    serializer=JobSerializer(instance=jobs)
    
    #Returns the data as a response 
    return Response({"JOBS":serializer.data})


#Api view to view any job
@api_view(['GET'])
def search_jobs(request,title):

    
    #checks if a user job with the title exist
    profile=Jobs.objects.filter(title=title)

    #Serializes the job data
    serializer=JobSerializer(instance=profile)
    
    #Returns the data as a response 
    return Response({"searchjob":serializer.data})