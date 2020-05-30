from django.urls import path, include
from rest_framework import routers
from imageupload_rest.viewsets import UploadedImagesViewSet

# Wire up our API with our urls
urlpatterns = [
    path('', UploadedImagesViewSet.as_view()),
]
