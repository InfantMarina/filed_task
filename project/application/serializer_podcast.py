from application import models
from rest_framework import serializers

class serializingtables(serializers.ModelSerializer):
    class Meta:
        model = models.Podcast
        # fields = ['Name_of_the_podcast','host']
        fields = "__all__"