from rest_framework import serializers
from application import models


class serializingtables(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = "__all__"
        # read_only_fields = ['Name_of_the_Song','Duration_in_number_of_seconds','Uploaded_time']
        # fields = ['Name_of_the_Song','Duration_in_number_of_seconds','Uploaded_time','File_path']
