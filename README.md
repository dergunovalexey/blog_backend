# RESTfil backend to simple blog

## Run project

1. Create env
> virtualenv -p python3.6 env

2. Activate env
> source env/bin/activate

3. Install packeges
> pip install -r requirements.txt

4. Create local settings file
> touch ./blog_backend/settings_local.py

5. Set local settings.
Copy settings from settings_local_example.py, set postgre and redis to project

6. Create tables
> ./manage.py migrate

7. Create superuser
> ./manage.py createsuperuser

8. Run server
> ./manage.py runserver
