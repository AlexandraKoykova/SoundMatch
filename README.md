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
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

The project follows Django's Model-View-Template (MVT) architecture and separates functionality into four applications.

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

Windows:

```bash
.venv\Scripts\activate
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

**6. Start the development server**

```bash
python manage.py runserver
```

Open the application at:

http://127.0.0.1:8000/

## 🗃️ Database Relationships

The application includes several Django models and relationships:

- **Artist ↔ Genre:** Many-to-Many relationship
- **Booking → Artist:** ForeignKey relationship
- **Review → Artist:** ForeignKey relationship

These relationships support artist discovery, booking management, and user reviews.

## 🎨 Design

SoundMatch features a modern, music-inspired interface with a dark navy background, purple accents, and neon-inspired visual elements.

The design emphasizes artist discovery and a simple booking experience.

## 📌 Project Purpose

This project was developed as part of the **Python Web Development learning path at SoftUni**.

Its purpose is to demonstrate practical knowledge of Django, including models, forms, class-based views, database relationships, CRUD operations, template inheritance, custom template filters, and form validation.

## 👩‍💻 Author

**Alexandra Koykova**

GitHub: https://github.com/AlexandraKoykova

---

*SoundMatch — Find your beat.*