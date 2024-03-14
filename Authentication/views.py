from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import UserProfile
from .serializer import UserSerializer,ResetPasswordEmailSerializer,PasswordResetConfirmSerializer,ProfileSerializer

from django.core.mail import send_mail
from django.utils import timezone
from .utils import generate_reset_token

from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model, views as auth_views
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect,render

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse


# from django.utils.http import urlsafe_base64_decode
# from django.http import Http404

# from django.contrib.auth.tokens import default_token_generator


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

        # Get UID for the user
        UserModel = get_user_model()
        user = UserModel.objects.get(email=email)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

        # Construct password reset URL with UID and token
        reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
        reset_link = request.build_absolute_uri(reset_url)

        # Send password reset email
        subject = 'Password Reset Request'
        message = f'Click the link below to reset your password:\n\n{reset_link}'
        from_email = 'ebubeidika@gmail.com'  # Use your email here
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        # Optionally save the token and timestamp associated with the user
        # You can add logic here to save them in the database if needed

        return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






@api_view(['POST'])
def password_reset_confirm(request):
    serializer=PasswordResetConfirmSerializer(data=request.data)

    if serializer.is_valid():
        pass

@api_view(['POST'])
def profile_add(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'profile': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
def profile_get(request):
    profiles = UserProfile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response({'profiles': serializer.data}, status=status.HTTP_200_OK)


@api_view(["PUT"])
def profile_update(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return Response({'error': 'Profile does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProfileSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'profile': serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
