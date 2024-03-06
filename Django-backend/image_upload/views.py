import cv2
import easyocr
import time
import requests
from django.http import JsonResponse
from django.conf import settings
import os

def perform_ocr(image_path):
    # Start OCR timer
    start_ocr_time = time.time()
    
    # Read image
    img = cv2.imread(image_path)
    reader = easyocr.Reader(['en'], gpu=True)
    text_ocr = reader.readtext(img)
    result = " ".join([t[1] for t in text_ocr if t[2] > 0.25])
    
    # End OCR timer 
    end_ocr_time = time.time()
    ocr_time = end_ocr_time - start_ocr_time
    print(f"Time taken for text detection: {ocr_time:.2f} seconds")
    print("Text Detected: ", result)
    
    return result
    
def search_book_google_api(query):
    # Start timer
    start_api_time = time.time()

    # Search for the top match
    google_books_api_url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": query, "maxResults": 1}  
    response = requests.get(google_books_api_url, params=params)

    # End timer 
    end_api_time = time.time()
    api_time = end_api_time - start_api_time
    print(f"Time taken for Google Books API: {api_time:.2f} seconds")
    return response

def extract_book_details(response):
    if response.status_code == 200:
        book_data = response.json()

        if 'items' in book_data and len(book_data['items']) > 0:
            book_info = book_data['items'][0]['volumeInfo']

            # Extracting relevant info
            title = book_info.get('title', 'N/A')
            authors = ', '.join(book_info.get('authors', ['N/A']))
            categories = ', '.join(book_info.get('categories', ['N/A']))
            maturityRating = book_info.get('maturityRat`ing', 'N/A')
            description = book_info.get('description', 'N/A')
            
            print(f"\nBook Details:")
            print(f"Title: {title}")
            print(f"Author: {authors}")
            print(f"Category: {categories}")
            print(f"Mature Rating: {maturityRating}")
            print(f"Description: {description}")

            
        else:
            return None
    else:
        print(f"\nFailed to retrieve book details. Status Code: {response.status_code}")
        return None


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
        
        # Perform OCR on the uploaded image
        text_data = perform_ocr(os.path.join(settings.MEDIA_ROOT, filename))
        
        # Query google books api with extracted textabs
        book=search_book_google_api(text_data)
        
        # Extract and print book details
        book_details = extract_book_details(book)

        
        # Return JSON response with OCR results
        return JsonResponse({'message': 'Image uploaded and OCR processed successfully.', 'filename': filename})
    else:
        return JsonResponse({'error': 'No image found in the request.'}, status=400)

