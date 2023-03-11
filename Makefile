server:
	python manage.py runserver 0.0.0.0:9001

migrate:
	python manage.py makemigrations
	python manage.py migrate

shell:
	python manage.py shell

install:
	pip install -r requirements.txt

start_ws_daemon:
	python manage.py start_client_ws

start_telegram_daemon:
	python manage.py start_telegram

target: server start_ws_daemon start_telegram_daemon

run:
	make -i -j3 target

