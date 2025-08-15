# Academy (Django) - Render Ready

## Local run
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata sample_data.json
python manage.py runserver
```

## Deploy on Render
1. Push this repo to GitHub.
2. On Render: New -> Web Service -> Connect this repo.
3. Start command: `gunicorn school_manager.wsgi`
4. Create a **PostgreSQL** on Render, copy its `External Database URL`.
5. Add env vars on the Web Service:
   - `DATABASE_URL` = the Postgres URL
   - `DEBUG` = `False`
   - `SECRET_KEY` = (generate a strong key)
6. After deploy, open Shell:
```bash
python manage.py migrate
python manage.py loaddata sample_data.json
python manage.py createsuperuser
```
