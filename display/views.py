from rest_framework import viewsets


from .models import Profile

from .serializers import ProfileSerializer

# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    """
    Django Viewset to display details of a profile
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
