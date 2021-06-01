from application import models
from rest_framework import serializers

class serializingtables(serializers.ModelSerializer):
    class Meta:
        model = models.Audio_Book
        fields = "__all__"