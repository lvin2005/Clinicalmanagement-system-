# Quick Setup Instructions

## 1. Install Dependencies
```bash
pip install -r requirements.txt
```

## 2. Database Setup
```sql
CREATE DATABASE event_portal_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'root'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON event_portal_db.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
```

## 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## 4. Create Superuser
```bash
python manage.py createsuperuser
```

## 5. Collect Static Files
```bash
python manage.py collectstatic
```

## 6. Run Server
```bash
python manage.py runserver
```

Access the application at: http://127.0.0.1:8000/

## URLs
- Home: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- Events: http://127.0.0.1:8000/events/
- Dashboard: http://127.0.0.1:8000/dashboard/
