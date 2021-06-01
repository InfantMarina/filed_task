from django.db import models

class Song(models.Model):
    Name_of_the_Song = models.CharField(max_length=100,null=False,blank=False)
    Duration_in_number_of_seconds = models.IntegerField(null=False,blank=False)
    Uploaded_time = models.DateTimeField(auto_now_add=True)
    File_path = models.CharField(max_length=1000,null=False,blank=False)

class Podcast(models.Model):
    Name_of_the_Podcast = models.CharField(max_length=100,null=False,blank=False)
    Duration_in_number_of_seconds = models.IntegerField(null=False,blank=False)
    Uploaded_time = models.DateTimeField(auto_now_add=True)
    Host = models.CharField(max_length=100,null=False,blank=False)
    Participants = models.CharField(max_length=100,null=True,blank=True)
    File_path = models.CharField(max_length=1000,null=False,blank=False)

class Audio_Book(models.Model):
    Title_of_the_Audiobook = models.CharField(max_length=100,null=False,blank=False)
    Author_of_the_Title = models.CharField(max_length=100,null=False,blank=False)
    Narrator = models.CharField(max_length=100,null=False,blank=False)
    Duration_in_number_of_seconds = models.IntegerField(null=False,blank=False)
    Uploaded_time = models.DateTimeField(auto_now_add=True)
    File_path = models.CharField(max_length=1000,null=False,blank=False)