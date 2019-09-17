# requirements
PostgreSQL, Python3
# setup
Create python virtual environment
```python -m venv venv```

Activate environment
```source venv/bin/activate```

Install Django, PostgreSQL adapter
```pip install django psycopg2```

Start PostgreSQL
```systemctl start postgresql.service```

Setup PostgreSQL for playground
```./execute_sql.sh playground_setup.sql```

Make directory for saved files
```mkdir /var/django_playground```

Change directory owner
```chown your-username /var/django_playground```

Make migrations
```python manage.py makemigrations```

Migrate
```python manage.py migrate```

Run server
```python manage.py runserver```

Open ```localhost:8000/files``` in browser, try to upload files (first file is in model and textbox with second file are in composite field which is in model)
