from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['listing_id', 'title', 'description', 'price_per_night', 'location', 'created_at', 'updated_at']
        read_only_fields = ['listing_id', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['booking_id', 'property', 'user_id', 'start_date', 'end_date', 'total_price', 'status', 'created_at', 'updated_at']
        read_only_fields = ['booking_id', 'total_price', 'created_at', 'updated_at']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['review_id', 'property', 'user_id', 'rating', 'comment', 'created_at', 'updated_at']
        read_only_fields = ['review_id', 'created_at', 'updated_at']
