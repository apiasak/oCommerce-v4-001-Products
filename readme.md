Install vitrual env
```python3 -m venv tutorial-env```

Activate virturn env
```source tutorial-env/bin/activate```

Install Django
```python3 -m pip install Django```

1. Create project
```django-admin startproject ocommerce```


2. Create App
```python manage.py startapp store_app```

3. Migrate db
```python manage.py migrate``

4. Create superuser
```python manage.py createsuperuser```