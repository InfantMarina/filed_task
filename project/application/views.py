import mutagen
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import View
from playsound import playsound
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from application import (serializer_audiobook, serializer_podcast, serializer_song)
from application.models import Audio_Book, Podcast, Song


class Main(APIView):
    
    def get(self, request, audioFileType=None, audioFileID=None):

        data = {}
        # get for song table
        if audioFileType and str(audioFileType).lower() == 'song':
            song_table = Song.objects.all()
            song_table_serializing = serializer_song.serializingtables(song_table, many=True)
            if audioFileID:
                try:
                    song_table = Song.objects.get(id=audioFileID)
                    song_table_serializing = serializer_song.serializingtables(song_table)
                except Song.DoesNotExist:
                    raise Http404
            data['song'] = song_table_serializing.data
            return Response(data, status=status.HTTP_200_OK)

        # get for podcast table
        if audioFileType and str(audioFileType).lower() == 'podcast':
            podcast_table = Podcast.objects.all()
            podcast_table_serilizing = serializer_podcast.serializingtables(podcast_table, many=True)
            if audioFileID:
                try:
                    podcast_table = Podcast.objects.get(id=audioFileID)
                    podcast_table_serilizing = serializer_podcast.serializingtables(podcast_table)
                except Podcast.DoesNotExist:
                    raise Http404
            data['podcast'] = podcast_table_serilizing.data
            return Response(data, status=status.HTTP_200_OK)

        # get for audiobook table
        if audioFileType and str(audioFileType).lower() == 'audiobook':
            audiobook_table = Audio_Book.objects.all()
            audiobook_table_serilizing = serializer_audiobook.serializingtables(audiobook_table, many=True)
            if audioFileID:
                try:
                    audiobook_table = Audio_Book.objects.get(id=audioFileID)
                    audiobook_table_serilizing = serializer_audiobook.serializingtables(audiobook_table)
                except Audio_Book.DoesNotExist:
                    raise Http404
            data['audiobook'] = audiobook_table_serilizing.data
            return Response(data, status=status.HTTP_200_OK)

        if request.accepted_renderer.format == 'html':
            return HttpResponse('get method called')
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, audioFileType=None, audioFileID=None):

        data = request.data
        # calculating the audio duration
        audio_length = mutagen.File(data['File_path']).info.length
        
        # finding the type of the song
        if 'Name_of_the_Song' in data.keys():
            # storing in song table
            song_table = Song()
            song_table.Name_of_the_Song = data['Name_of_the_Song']
            song_table.File_path = data['File_path']
            song_table.Duration_in_number_of_seconds = audio_length
            song_table.save()
            return Response(status=status.HTTP_200_OK)
        
        if 'Name_of_the_Podcast' in data.keys():
            # storing in podcast table
            podcast_table = Podcast()
            podcast_table.Name_of_the_Podcast = data['Name_of_the_Podcast']
            podcast_table.File_path = data['File_path']
            podcast_table.Host = data['Host']
            podcast_table.Duration_in_number_of_seconds = audio_length
            podcast_table.save()
            return Response(status=status.HTTP_200_OK)

        if 'Title_of_the_Audiobook' in data.keys():
            # storing in audiobook table
            audiobook_table = Audio_Book()
            audiobook_table.Title_of_the_Audiobook = data['Title_of_the_Audiobook']
            audiobook_table.Author_of_the_Title = data['Author_of_the_Title']
            audiobook_table.File_path = data['File_path']
            audiobook_table.Narrator = data['Narrator']
            audiobook_table.Duration_in_number_of_seconds = audio_length
            audiobook_table.save()
            return Response(status=status.HTTP_200_OK)

        if request.accepted_renderer.format == 'html':
            return HttpResponse('post method called')
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, audioFileType=None, audioFileID=None):

        data = request.data
        if audioFileType and str(audioFileType).lower() == 'song':
            try:
                song_table = Song.objects.get(id=audioFileID)
                song_table_serializing = serializer_song.serializingtables(song_table, data=data, partial=True)
                if song_table_serializing.is_valid():
                    song_table_serializing.save()
                else:
                    return Response(song_table_serializing.error_messages)
            except Song.DoesNotExist:
                raise Http404
            return Response(status=status.HTTP_200_OK)

        if audioFileType and str(audioFileType).lower() == 'podcast':
            try:
                podcast_table = Podcast.objects.get(id=audioFileID)
                podcast_table_serializing = serializer_podcast.serializingtables(podcast_table, data=data, partial=True)
                if podcast_table_serializing.is_valid():
                    podcast_table_serializing.save()
                else:
                    return Response(song_table_serializing.error_messages)
            except Podcast.DoesNotExist:
                raise Http404
            return Response(status=status.HTTP_200_OK)

        if audioFileType and str(audioFileType).lower() == 'audiobook':
            try:
                audiobook_table = Audio_Book.objects.get(id=audioFileID)
                audiobook_table_serializing = serializer_audiobook.serializingtables( audiobook_table, data=data, partial=True)
                if  audiobook_table_serializing.is_valid():
                    audiobook_table_serializing.save()
                else:
                    return Response(song_table_serializing.error_messages)
            except Audio_Book.DoesNotExist:
                return Http404
            return Response(status=status.HTTP_200_OK)

        if request.accepted_renderer.format == 'html':
            return HttpResponse('put method called')
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
    def delete(self, request, audioFileType=None, audioFileID=None):
        
        if audioFileType and str(audioFileType).lower() == 'song':
            try:
                song_table = Song.objects.get(id=audioFileID)
                song_table.delete()
                return Response(status=status.HTTP_200_OK)
            except Song.DoesNotExist:
                raise Http404

        if audioFileType and str(audioFileType).lower() == 'podcast':
            try:
                podcast_table = Podcast.objects.get(id=audioFileID)
                podcast_table.delete()
                return Response(status=status.HTTP_200_OK)
            except Song.DoesNotExist:
                raise Http404

        if audioFileType and str(audioFileType).lower() == 'audiobook':
            try:
                audiobook_table = Audio_Book.objects.get(id=audioFileID)
                audiobook_table.delete()
                return Response(status=status.HTTP_200_OK)
            except Song.DoesNotExist:
                raise Http404

        if request.accepted_renderer.format == 'html':
            return HttpResponse('delete method called')
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
