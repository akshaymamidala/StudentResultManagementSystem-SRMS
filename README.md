# SRMS - Student Result Management System

A Django-based web application to manage students, branches, subjects, notices, and semester-wise results.

## Features

- Student login using hall ticket number + semester
- Student result view (subject-wise internal, external, total marks)
- Admin login dashboard
- CRUD for students, subjects, branches, notices, and results
- Student search and result search by hall ticket number
- Bulk student import via `.xlsx`
- SQLite database (easy local setup)

## Tech Stack

- Python
- Django
- SQLite
- django-crispy-forms
- django-import-export + tablib
- django-autoslug

## Prerequisites

Install these before running:

- Python `3.12+` recommended
- `pip`
- `git`

> This project uses `django==6.0.3` from `requirements.txt`.

## 1) Clone the Repository

```bash
git clone https://github.com/akshaymamidala/StudentResultManagementSystem-SRMS
cd srms
```

## 2) Create and Activate Virtual Environment

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Windows (CMD)

```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3) Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 4) Apply Database Migrations

```bash
python manage.py migrate
```

## 5) Create Admin User (Recommended)

```bash
python manage.py createsuperuser
```

Follow the prompt to set username, email, and password.

## 6) Run the Development Server

```bash
python manage.py runserver
```

Open:

- Home: `http://127.0.0.1:8000/`
- Django Admin: `http://127.0.0.1:8000/admin/`
- App Admin Login: `http://127.0.0.1:8000/sadmin/login/`
- Student Login: `http://127.0.0.1:8000/student/login/`

## How to Use the Project

### Student Flow

1. Open `/student/login/`
2. Enter hall ticket number and semester
3. View semester result table

### Admin Flow

1. Open `/sadmin/login/` and sign in
2. Go to dashboard `/sadmin/page/`
3. Manage modules:
   - Students: `/student/`
   - Subjects: `/subject/`
   - Branches: `/branch/`
   - Notices: `/notices/`
   - Results: `/result/`

## Bulk Import

### Student Import

- Page: `/student/import`
- File type: `.xlsx`
- Triggered from **Students -> Bulk Import**

## Important Notes

- Default database is SQLite (`db.sqlite3`).
- If your repo includes an old `db.sqlite3`, you can still run `migrate` safely.
- `SECRET_KEY` and `DEBUG=True` are currently set for local development only.
- Do not use current settings directly in production.

## Common Troubleshooting

### `python` command not found

- Windows: install Python and check "Add Python to PATH"
- macOS/Linux: use `python3` instead of `python`

### Migration errors

```bash
python manage.py makemigrations
python manage.py migrate
```

### Port already in use

```bash
python manage.py runserver 8001
```

### Static files not loading

Ensure `django.contrib.staticfiles` is enabled (already configured in `srms/settings.py`) and run server from project root.

## Project Structure

```text
srms/
|-- manage.py
|-- requirements.txt
|-- db.sqlite3
|-- srms/              # Django project config (settings, urls, wsgi)
|-- result/            # Main app (models, views, forms, templates, static)
```



