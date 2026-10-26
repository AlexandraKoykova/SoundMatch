# 🎤 SoundMatch – Smart Artist Booking Platform

**SoundMatch** is a Django-based web application designed to connect artists with event organizers and clients looking for live entertainment.

The platform allows users to explore musical talent, discover artists by genre, compare booking prices, and submit booking requests through an intuitive interface.

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
- Add new genres
- View artists associated with each genre
- Load initial music genres using a JSON fixture

### Review Management
- Submit artist reviews
- Rate artists from 1 to 5
- Browse reviews and view review details

### Additional Functionality
- Responsive dark-themed interface
- Custom Django template filter for euro price formatting
- Custom 404 error page
- Template inheritance and reusable styling
- Form validation and error handling
- Initial database data provided through `genres.json`

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
├── requirements.txt
└── README.md
```

The project follows Django's Model-View-Template (MVT) architecture and separates functionality into four applications.

Uploaded media files are stored locally and are not included in the repository.

## 🚀 Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/AlexandraKoykova/SoundMatch.git
cd SoundMatch
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate the virtual environment**

Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Windows (Command Prompt):

```cmd
.venv\Scripts\activate.bat
```

macOS/Linux:

```bash
source .venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Apply database migrations**

```bash
python manage.py migrate
```

This command creates the necessary database tables for artists, bookings, genres, and reviews.

**6. Load initial music genres**

```bash
python manage.py loaddata genres.json
```

This command loads three initial music genres into the database.

The genres will then be available in the **Add Artist** form, allowing users to assign music genres when creating artist profiles.

**7. Start the development server**

```bash
python manage.py runserver
```

Open the application at:

http://127.0.0.1:8000/

**Important:** The SQLite database is created locally. Existing artist profiles, bookings, reviews, and uploaded images are not included in the repository.

## 🧪 Testing

The application can be tested manually by running the development server and checking the main features.

Recommended checks:

- Create, edit, and delete artist profiles
- Search and filter artists by genre
- Sort artists by booking price
- Create and manage bookings
- Test booking form validations
- Add music genres and reviews
- Verify that custom template filters work correctly
- Verify that the custom 404 page is displayed for invalid URLs

To run automated Django tests, use:

```bash
python manage.py test
```

Django uses a separate test database to execute the tests without modifying the application's normal database.

## 🗃️ Database Relationships

The application includes several Django models and relationships:

- **Artist ↔ Genre:** Many-to-Many relationship
- **Booking → Artist:** ForeignKey relationship
- **Review → Artist:** ForeignKey relationship

These relationships support artist discovery, booking management, and user reviews.

### Initial Database Data

The repository includes a `genres.json` fixture containing three music genres.

After installing the application and applying migrations, users can populate the genre table by running:

```bash
python manage.py loaddata genres.json
```

This ensures that the artist creation form has available music genres even when the project is installed on a new computer.

## 🎨 Design

SoundMatch features a modern, music-inspired interface with a dark navy background, purple accents, and neon-inspired visual elements.

The design emphasizes artist discovery and a simple booking experience.

## 📌 Project Purpose

This project was developed as part of the **Python Web Development learning path at SoftUni**.

Its purpose is to demonstrate practical knowledge of Django, including:

- Models and database relationships
- Class-based views
- Django forms and validation
- CRUD operations
- Template inheritance
- Custom template filters
- Searching, filtering, and sorting
- Database migrations and fixtures
- Custom error handling
- Git version control

## 👩‍💻 Author

**Alexandra Koykova**

GitHub: https://github.com/AlexandraKoykova

---

*SoundMatch — Find your beat.*t.*