# Django Todo App

A simple Django todo project with create, complete, and delete actions.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Features

- Add todo items
- Mark todo items complete or incomplete
- Delete todo items
- SQLite database for local development
- Django admin support for todos
