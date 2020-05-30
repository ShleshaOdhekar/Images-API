from rest_framework import viewsets, filters
from imageupload_rest.serializers import UploadedImageSerializer
from imageupload.models import UploadedImage
from rest_framework.response import Response
from rest_framework.views import APIView




# ViewSet for our UploadedImage Model
# Gets all images from database and serializes them using UploadedImageSerializer
class UploadedImagesViewSet(APIView):

    def get(self, request, *args, **kwargs):
        qs= UploadedImage.objects.all()
        serializer= UploadedImageSerializer(qs, many=True) 
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer= UploadedImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

