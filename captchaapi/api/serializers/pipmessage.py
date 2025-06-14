from rest_framework import serializers
from api.models import PipMsg


class PipMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = PipMsg
        fields = '__all__'
