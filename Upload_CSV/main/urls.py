from django.urls import path, include
from .views import *

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('show_all/', show_all, name='show_all'),
]