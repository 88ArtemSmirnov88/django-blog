make start:
	python manage.py runserver

make migrations:
	python manage.py makemigrations

make migrate:
	python manage.py migrate

make repl:
	python manage.py shell
