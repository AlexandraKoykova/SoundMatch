# 🎤 SoundMatch – Smart Artist Booking Platform

**SoundMatch** is a Django-based web application designed to connect artists with event organizers and clients looking for live entertainment.

The platform allows users to explore musical talent, discover artists by genre, compare booking prices, and submit booking requests through an intuitive interface.

The application is developed as an individual project for the **Django Basics course at SoftUni**.

## ✨ Features

### Artist Management
- Browse available artist profiles
- View artist details, genres, and booking prices
- Create, edit, and delete artist profiles
- Upload artist profile images
- Search artists by stage name
- Filter artists by music genre
- Sort artists by price or name

### Booking Management
- Submit booking requests for artists
- View booking details
- Edit and delete bookings
- Manage booking statuses: Pending, Confirmed, Rejected
- Validate event dates and prevent conflicting confirmed bookings

### Genre Management
- Browse music genres
- Create new genres through the application interface
- View artists associated with each genre
- Optionally load initial genres using a JSON fixture

### Review Management
- Submit artist reviews
- Rate artists from 1 to 5
- Browse reviews and view review details

### Additional Functionality
- Responsive dark-themed interface
- Custom Django template filter for euro price formatting
- Custom 404 error page
- Template inheritance and reusable styling
- Form validation and user-friendly error messages
- Search, filtering, and sorting functionality
- Optional sample data through JSON fixtures

## 🛠️ Technologies Used

- Python 3
- Django
- SQLite
- HTML