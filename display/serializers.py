from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer class for displaying the details of the profile
    """
    class Meta:
        model = Profile
        fields = '__all__'