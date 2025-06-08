from rest_framework import viewsets
from api.models import UserActivity
from api.serializers import UserActivitySerializer


class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer
