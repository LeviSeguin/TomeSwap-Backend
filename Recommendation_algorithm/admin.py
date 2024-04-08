#Recommendation_algorithm/admin
from django.contrib import admin
from .models import *
admin.site.register(BookInteraction)
admin.site.register(Book)