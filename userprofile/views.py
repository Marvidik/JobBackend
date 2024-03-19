from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(["POST"])
def create_profile(request):
    pass


def view_profile(request):
    pass


def update_profile(request):
    pass



