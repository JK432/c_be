from rest_framework import viewsets
from api.models import PipMsg
from api.serializers import PipMsgSerializer


class PipMsgViewSet(viewsets.ModelViewSet):
    queryset = PipMsg.objects.all()
    serializer_class = PipMsgSerializer
