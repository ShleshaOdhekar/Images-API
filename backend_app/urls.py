from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from imageupload import views
# Routing of our Django App

urlpatterns = [
    
    path('admin/', admin.site.urls),
    # anything going to /api gets redirected to the django rest API stuff
    path('api/', include('imageupload_rest.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# we are serving static and media files here at the moment - if we deploy this app to a server, we do necessarily want this

