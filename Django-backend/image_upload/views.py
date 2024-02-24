from django.shortcuts import render
from django.http import JsonResponse


def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        # Process the uploaded image, e.g., save it to storage
        # You may want to use Django's FileSystemStorage or any other storage backend
        # For simplicity, let's assume we're saving the image to a media folder
        with open('media/uploaded_image.jpg', 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
        return JsonResponse({'message': 'Image uploaded successfully.'})
    else:
        return JsonResponse({'error': 'No image found in the request.'}, status=400)