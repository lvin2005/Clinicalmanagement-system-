# Quick Run Instructions

## Virtual Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django
```

## Database Setup
```bash
# Run migrations
python manage.py migrate

# Create superuser (admin/admin123)
python manage.py createsuperuser --username admin --email admin@example.com
# Set password: admin123
```

## Run Server
```bash
# Start development server
python manage.py runserver 127.0.0.1:8000
```

## Access the Application
- **Home Page**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
  - Username: admin
  - Password: admin123
- **Events**: http://127.0.0.1:8000/events/
- **Dashboard**: http://127.0.0.1:8000/dashboard/

## Test Features
1. Browse the home page
2. View events list
3. Register a new user account
4. Login and access dashboard
5. Access admin panel to manage content

## Notes
- Currently using SQLite database for easy testing
- Static files are configured and collected
- Bootstrap 5 is loaded locally
- All Django apps are properly configured
