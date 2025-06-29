from rest_framework import viewsets
from api.models import UserActivity
from api.serializers import UserActivitySerializer
from django_filters.rest_framework import FilterSet
from django.conf import settings

class UserActivityFilter(FilterSet):
    class Meta:
        model = UserActivity
        fields = {
            'mode': settings.FILTER_NUMBER_MODELS,
        }

class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer
    filterset_class = UserActivityFilter