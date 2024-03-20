from django.http import JsonResponse
from image_upload.models import listing

def fetch_listing(request):
    # Fetch data from the 'listing' model
    listings = listing.objects.all()
    
    # Serialize the data
    serialized_listings = [{
        'title': item.title,
        'authors': item.authors,
        'categories': item.categories,
        'username': item.username,
        'listingid': item.listingid,
        'thumbnail': item.thumbnail
    } for item in listings]
    
    # Return the serialized data as a JSON response
    return JsonResponse(serialized_listings, safe=False)
