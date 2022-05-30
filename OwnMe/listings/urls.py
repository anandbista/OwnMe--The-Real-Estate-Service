
from django.urls import path
from .views import (ListingListView, ListingDetailView, search)
from . import views


urlpatterns = [
    path('', ListingListView.as_view(), name='listings'),
    path('<int:pk>', ListingDetailView.as_view(), name='listing'),
    path('add_listing/', views.add_listing, name='add-listing'),
    path('search', search, name='search'),
   
]
