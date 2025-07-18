Markdown

# alx_travel_app_0x00

## Overview

This project is a Django-based travel application. It includes models for listings, bookings, and reviews, an API for data representation, and a management command to seed the database with sample data.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/Tabbytech/alx_travel_app_0x00/tree/main>
   cd alx_travel_app_0x00

Create a virtual environment (recommended):

Bash

python -m venv venv
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate  # On Windows
Install dependencies:

Bash

pip install -r requirements.txt

Navigate to the project directory:

Bash

cd alx_travel_app_0x00
Apply migrations:

Bash

python manage.py migrate
Create a superuser (optional but recommended for admin access):

Bash

python manage.py createsuperuser
Running the Application
Start the development server:

Bash

python manage.py runserver
Access the application in your web browser:
Open your browser and go to http://127.0.0.1:8000/.

Running the Management Command (Seeder)
To populate the database with sample listings, run the following command:

Bash

python manage.py seed
API Endpoints (Example - you'll need to define these in your urls.py)
/api/listings/: To view and create listings.

/api/bookings/: To view and create bookings.


Models
Listing: Represents a property available for booking.

Booking: Represents a reservation made by a user for a listing.

Review: Represents a review given by a user for a listing.

Serializers
Serializers are used to convert model instances to JSON format for the API.

ListingSerializer: For the Listing model.

BookingSerializer: For the Booking model.

ReviewSerializer: For the Review model.
