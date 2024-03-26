from django.http import JsonResponse
from image_upload.models import listing
from django.db.models import Q

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
        'thumbnail': item.thumbnail,
        'description': item.description,
    } for item in listings]
    
    # Return the serialized data as a JSON response
    return JsonResponse(serialized_listings, safe=False)

def search_listing(request):
    # Get the search query from the request parameters
    search_query = request.GET.get('q', '')

    # Output debug message to console
    print(f"Search query: {search_query}")

    # Fetch data from the 'Listing' model based on the search query
    listings = listing.objects.filter(
        Q(title__icontains=search_query) |  # Search in title
        Q(authors__icontains=search_query) |  # Search in authors
        Q(categories__icontains=search_query) |  # Search in categories
        Q(username__icontains=search_query) |  # Search in username
        Q(description__icontains=search_query)  # Search in description
    )

    # Output debug message to console
    print(f"Number of listings found: {listings.count()}")

    # Serialize the filtered data
    serialized_listings = [{
        'title': item.title,
        'authors': item.authors,
        'categories': item.categories,
        'username': item.username,
        'listingid': item.listingid,
        'thumbnail': item.thumbnail,
        'description': item.description,
    } for item in listings]


    # Return the serialized data as a JSON response
    return JsonResponse(serialized_listings, safe=False)