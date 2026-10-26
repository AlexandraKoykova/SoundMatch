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
- HTML5
- CSS3
- Django Template Language (DTL)
- Git & GitHub

## 📁 Project Structure

```text
SoundMatch/
├── artists/
├── bookings/
├── genres/
├── reviews/
├── sound_match/
├── templates/
├── static/
├── manage.py
├── genres.json
├── artists.json
├── requirements.txt
└── README.md
```

The project follows Django's Model-View-Template (MVT) architecture and separates functionality into four Django applications:

- **artists** — Artist profiles, management, search, filtering, and sorting
- **bookings** — Booking requests, management, and validation
- **genres** — Music genre management and artist categorization
- **reviews** — Artist reviews and ratings

Uploaded media files are stored locally and are not automatically included in the repository.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/AlexandraKoykova/SoundMatch.git
cd SoundMatch
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```cmd
.venv\Scripts\activate.bat
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

This command creates the necessary database tables for artists, bookings, genres, and reviews.

The application is designed to work with an empty database. All required objects can be created manually through the web interface.

### 6. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

### 7. Optional: Load sample data

For demonstration purposes, the repository may include JSON fixtures containing sample genres and artists.

To load initial music genres:

```bash
python manage.py loaddata genres.json
```

To load sample artists:

```bash
python manage.py loaddata artists.json
```

**Important:**
- Loading fixtures is optional.
- The application does not require prepopulated data to function.
- All required objects can be created through the user interface.
- Genres must be loaded before artists when using the sample fixtures.
- Artist image files are not included in JSON fixtures and must be provided separately if needed.
- These commands should only be used if the corresponding fixture files are available in the repository.

### Local Configuration

The application uses SQLite for local development and does not require a separate database server.

No user registration or authentication is required.

If the project configuration requires environment variables or credentials, they must be documented here before submission.

## 🧪 Manual Testing

The application can be tested manually through its web interface.

After completing the installation steps, users can:

- Create music genres through the navigation menu
- Create artist profiles and assign genres
- Upload artist images
- Edit and delete artist profiles
- Search artists by stage name
- Filter artists by genre
- Sort artists by booking price or name
- Submit booking requests
- Edit bookings and update their statuses
- Test booking date validations
- Add artist reviews and ratings
- Navigate between artist, booking, genre, and review pages
- Verify form validation messages
- Verify the custom 404 error page

### Testing with an Empty Database

To verify the application without sample data:

1. Clone the repository into a new directory.
2. Install the dependencies.
3. Apply the database migrations.
4. Start the development server without loading fixtures.
5. Create a genre through the application interface.
6. Create an artist and assign the new genre.
7. Create a booking for that artist.
8. Submit a review for the artist.
9. Test the available editing, deletion, searching, and filtering functionality.

This workflow allows the application to be evaluated without using the Django admin panel or manually modifying the database.

## 🗃️ Database Models and Relationships

The application contains four main models:

### Artist
Stores information about performers, including their stage names, biographies, music genres, booking prices, and profile images.

### Genre
Represents musical genres used to categorize artists.

### Booking
Stores booking requests for artists, including event information and booking statuses.

### Review
Stores artist reviews and ratings.

### Database Relationships

- **Artist ↔ Genre:** Many-to-Many relationship
- **Booking → Artist:** ForeignKey relationship
- **Review → Artist:** ForeignKey relationship

These relationships allow artists to belong to multiple genres and to receive multiple bookings and reviews.

## 🎨 Design

SoundMatch features a modern, music-inspired interface with:

- Dark navy backgrounds
- Purple and pink accents
- Neon-inspired visual elements
- Artist profile cards
- Responsive layouts
- Consistent navigation and styling

The design emphasizes artist discovery and a simple booking experience.

## 📌 Project Purpose

This project was developed as part of the **Python Web Development learning path at SoftUni**.

Its purpose is to demonstrate practical knowledge of Django fundamentals, including:

- Django models and database relationships
- Class-based views
- Django forms and validation
- CRUD operations
- Template inheritance
- Custom template filters
- Searching, filtering, and sorting
- Database migrations
- Optional fixtures
- Custom error handling
- Git version control
- Clean and modular project structure

## 👩‍💻 Author

**Alexandra Koykova**

GitHub: https://github.com/AlexandraKoykova

---

*SoundMatch — Find your beat.*