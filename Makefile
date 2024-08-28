run:
	@$(MAKE) up_pg
	@$(MAKE) migrate
	@$(MAKE) fill_db
	python manage.py runserver

newapp:
	python manage.py startapp mainapp

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

up_pg:
	@docker compose up -d pg

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

fill_fake:
	python manage.py fake_factory_boy

go:
	docker start lesson_11_zoo-pg-1

redis_go:
	docker compose up -d redis

worker_go:
	python manage.py rqworker

queue_statistic:
	python manage.py rqstats --interval=1

api_go:
	python manage.py startapp api

start:
	python manage.py runserver
