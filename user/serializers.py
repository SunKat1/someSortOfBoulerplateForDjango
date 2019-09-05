from .models import UserAccount
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = UserAccount
    fields = ['email', 'username', 'avatar', 'role', 'is_admin', 'is_staff']