import os
import uuid
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        
        # Determine the next sequential filename
        upload_count = len(os.listdir(settings.MEDIA_ROOT)) + 1
        filename = f"upload{upload_count}.{image_file.name.split('.')[-1]}"
        
        # Save the uploaded image to the media folder with the sequential filename
        with open(os.path.join(settings.MEDIA_ROOT, filename), 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
        
        return JsonResponse({'message': 'Image uploaded successfully.', 'filename': filename})
    else:
        return JsonResponse({'error': 'No image found in the request.'}, status=400)