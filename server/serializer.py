from rest_framework import serializers
from .models import FaceIdentity

class FaceIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceIdentity
        fields = "__all__"