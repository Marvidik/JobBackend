# utils.py
from django.utils import timezone
import secrets

def generate_reset_token():
    token = secrets.token_urlsafe(64)  # Generate a random URL-safe token
    timestamp = timezone.now()  # Get the current timestamp
    return token, timestamp
