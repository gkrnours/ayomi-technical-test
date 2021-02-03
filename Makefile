start:
	docker-compose up -d

stop:
	docker-compose down

build:
	docker-compose build

db:
	docker-compose exec backend python manage.py migrate