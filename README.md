# Remind Me Later API

A simple Django REST Framework (DRF) API to create reminders. Each reminder belongs to a user and stores a message, date, time, and reminder type (email or SMS).

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/remind-me-later-api.git
   cd remind-me-later-api
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for managing users in admin):**
   ```bash
   python manage.py createsuperuser
   ```
6. **Create a test user (optional):**
   ```bash
   python manage.py shell
   from django.contrib.auth.models import User
   user = User.objects.create(username="abhi", password="123")
   print(user.id)
   ```
7. **Run the server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Create Reminder
**POST** `/api/reminder/`

**Request body:**
```json
{
  "user": 1,
  "message": "Doctor Appointment",
  "date": "2025-08-23",
  "time": "17:45:00",
  "reminder_type": "email"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "user": 1,
  "message": "Doctor Appointment",
  "date": "2025-08-23",
  "time": "17:45:00",
  "reminder_type": "email"
}
```

### Get All Reminders
**GET** `/api/reminder/`

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "user": 1,
    "message": "Doctor Appointment",
    "date": "2025-08-23",
    "time": "17:45:00",
    "reminder_type": "email"
  },
  {
    "id": 2,
    "user": 1,
    "message": "Meeting with team",
    "date": "2025-08-24",
    "time": "09:30:00",
    "reminder_type": "sms"
  }
]
```
