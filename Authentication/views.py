from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Jobs

from .serializer import JobsSerializer, UserSerializer,ResetPasswordEmailSerializer

from django.core.mail import send_mail
from django.utils import timezone
from .utils import generate_reset_token



@api_view(['POST'])
def login(request):
    user=get_object_or_404(User,username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"details":"Info Not Found"})
    token,created=Token.objects.get_or_create(user=user)
    serializer=UserSerializer(instance=user)
    return Response({"token":token.key,"user":serializer.data})
  

@api_view(['POST'])
def register(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user=User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token=Token.objects.create(user=user)
        return Response({"token":token.key,"user":serializer.data})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def password_reset(request):
    serializer = ResetPasswordEmailSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.validated_data['email']

        # Generate reset token and timestamp
        token, timestamp = generate_reset_token()

        # Send password reset email
        subject = 'Password Reset Request'
        message = f'Click the link below to reset your password:\n\nhttp://127.0.0.1:8000/password/reset/?token={token}'
        from_email = 'ebubeidika@gmail.com'  # Use your email here
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        # Here you can add logic to save the token and timestamp
        # associated with the user in the database if needed

        return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# # Api for listing the jobs appears here 
# @api_view(["GET","POST","PUT","DELETE"])
# def jobs(request):
    
#     if request.method=="GET":
#         job=Jobs.objects.all()
#         serializer=JobsSerializer(instance=job, many=True)

#         return Response({"jobs":serializer.data})
    
#     if request.method=="POST":
#         serializer=JobsSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#         return Response({"job":serializer.data})

#     if request.method=="PUT":
#         obj=serializer.request.data["id"]
#         serializer=JobsSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#         return Response({"job":serializer.data})

#     else:
#         pass




