.PHONY: start stop

start: artifacts/db artifacts/build_backend
	docker-compose up -d

stop:
	docker-compose down
	rm artifacts/db

artifacts/build_backend: backend/requirements.txt
	docker-compose build backend
	touch artifacts/build_backend

artifacts/db: artifacts/build_backend
	docker-compose run --rm backend python manage.py migrate
	touch artifacts/db