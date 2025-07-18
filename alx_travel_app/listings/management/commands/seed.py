from django.core.management.base import BaseCommand
from listings.models import Listing
import uuid

class Command(BaseCommand):
    help = 'Populates the database with sample listing data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating sample listings...'))

        listings_data = [
            {
                'title': 'Cozy Apartment in City Center',
                'description': 'A comfortable and well-equipped apartment perfect for city exploration.',
                'price_per_night': 120.00,
                'location': 'New York, USA',
            },
            {
                'title': 'Luxury Villa with Ocean View',
                'description': 'Indulge in a luxurious stay with breathtaking ocean views.',
                'price_per_night': 550.00,
                'location': 'Bali, Indonesia',
            },
            {
                'title': 'Charming Cottage in the Countryside',
                'description': 'Escape to a peaceful countryside cottage surrounded by nature.',
                'price_per_night': 85.00,
                'location': 'Cotswolds, UK',
            },
            {
                'title': 'Modern Loft in Downtown Area',
                'description': 'Experience urban living in this stylish and modern loft.',
                'price_per_night': 180.00,
                'location': 'Tokyo, Japan',
            },
            {
                'title': 'Historic House in Old Town',
                'description': 'Step back in time in this beautifully preserved historic house.',
                'price_per_night': 150.00,
                'location': 'Prague, Czech Republic',
            },
        ]

        for listing_info in listings_data:
            Listing.objects.create(**listing_info)

        self.stdout.write(self.style.SUCCESS('Successfully created sample listings.'))
