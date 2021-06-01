from django.contrib import admin
from django.urls import include, path, re_path

from application import views

# from rest_framework import routers

app_name = "application"

# router = routers.DefaultRouter()
# router.register('audio', views.Main, basename='main')

urlpatterns = [
    # re_path('^$', views.Main.as_view(), name="main")
    re_path('audio_file/?(?P<audioFileType>(song|podcast|audiobook))?/?(?P<audioFileID>[0-9]{1,4})?/?$', views.Main.as_view(),name="main"),
    # path('',include(router.urls))
]
