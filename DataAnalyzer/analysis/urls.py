from django.urls import path
from . import views

# Define the URL patterns for the application
urlpatterns = [
    # Map the root URL to the upload_file view and name it 'upload_file'
    path('', views.upload_file, name='upload_file'),
]
