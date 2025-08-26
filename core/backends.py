# core/backends.py
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import MultipleObjectsReturned
from .models import Users




class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        email = kwargs.get("email") or username
        if not email or not password:
            return None
        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return None
        except MultipleObjectsReturned:
            return None
        
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None