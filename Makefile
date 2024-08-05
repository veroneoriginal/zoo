run:
	python manage.py runserver

newapp:
	python manage.py startapp mainapp

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py create_admin

fill_db:
	python manage.py fill_db

test:
	python manage.py test

coverage:
	coverage run --source='.' manage.py test
	coverage report --omit='settings/asgi.py, settings/wsgi.py, manage.py, mainapp/management/*' --fail-under=50
	coverage html --omit='settings/asgi.py, settings/wsgi.py, manage.py, mainapp/management/*'

lint:
	pylint $(shell git ls-files '*.py')