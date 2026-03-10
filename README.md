# Event Portal - Django Event Management Application

A complete, fully functional Django 5 web application for event management with user authentication, MySQL database, and modern responsive UI.

## Features

- **User Authentication**: Registration, login, logout with Django's built-in auth system
- **Event Management**: Create, view, and manage events
- **Booking System**: Book tickets for events with user dashboard
- **Blog**: Read blog posts with detailed views
- **Contact Form**: Contact page with message storage
- **Admin Panel**: Full admin interface for managing all content
- **Responsive Design**: Modern UI with Bootstrap 5 (local files)
- **MySQL Database**: Configured for production-ready deployment

## Project Structure

```
event_portal/
├── manage.py
├── event_portal/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── accounts/          # User authentication
├── events/            # Event management
├── bookings/          # Booking system
├── pages/             # Static pages and dashboard
├── blog/              # Blog functionality
├── contact/           # Contact form
├── templates/         # HTML templates
├── static/           # CSS, JS, images
└── requirements.txt  # Python dependencies
```

## Installation

### Prerequisites

- Python 3.8+
- MySQL 5.7+ or 8.0+
- pip

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd event_portal
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   
   Create MySQL database:
   ```sql
   CREATE DATABASE event_portal_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'root'@'localhost' IDENTIFIED BY 'password';
   GRANT ALL PRIVILEGES ON event_portal_db.* TO 'root'@'localhost';
   FLUSH PRIVILEGES;
   ```

5. **Configure Database**
   
   Update `event_portal/settings.py` with your MySQL credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'event_portal_db',
           'USER': 'root',
           'PASSWORD': 'password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

9. **Run development server**
   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`

## Usage

### Admin Panel
- Access at `http://127.0.0.1:8000/admin/`
- Use your superuser credentials to log in
- Manage events, bookings, blog posts, and contact messages

### User Features
- **Registration**: Sign up for a new account
- **Login/Logout**: Access your personal dashboard
- **Browse Events**: View all available events
- **Book Events**: Register for events with ticket selection
- **Dashboard**: View your bookings and upcoming events
- **Blog**: Read blog posts
- **Contact**: Send messages through the contact form

### URL Structure

- `/` - Home page
- `/about/` - About page
- `/services/` - Services page
- `/events/` - Event listing
- `/events/<id>/` - Event details
- `/bookings/create/<event_id>/` - Book tickets for an event
- `/bookings/my/` - User's bookings
- `/blog/` - Blog listing
- `/blog/<id>/` - Blog post details
- `/contact/` - Contact page
- `/accounts/login/` - User login
- `/accounts/signup/` - User registration
- `/accounts/logout/` - User logout
- `/dashboard/` - User dashboard (login required)

## Dependencies

See `requirements.txt` for the complete list of dependencies:

- Django 5.0+
- mysqlclient
- Pillow (for image handling)

## Development

### Running Tests
```bash
python manage.py test
```

### Creating New Apps
```bash
python manage.py startapp app_name
```

### Adding Static Files
Place CSS, JS, and images in the `static/` directory:
- `static/css/` - Stylesheets
- `static/js/` - JavaScript files
- `static/images/` - Image files

### Templates
All HTML templates are in the `templates/` directory with proper app subdirectories.

## Deployment

### Production Settings

1. **Security Settings**:
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`
   - Set up `SECRET_KEY` environment variable

2. **Database**:
   - Use production MySQL credentials
   - Ensure proper database permissions

3. **Static Files**:
   - Configure static file serving (e.g., whitenoise, nginx)
   - Run `collectstatic` for production

4. **WSGI Server**:
   - Use Gunicorn or uWSGI for production
   - Configure with nginx or Apache

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions, please use the contact form in the application or create an issue in the repository.
