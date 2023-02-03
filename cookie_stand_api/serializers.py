from rest_framework import serializers
from .models import CookieStand


class CookieStandSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = CookieStand
