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

start_control_bet_daemon:
	python manage.py start_control_bet

start_go_ws_daemon:
	./teste

export_env:
	source source_double/environment/env_export

target: export_env server start_telegram_daemon start_control_bet_daemon start_go_ws_daemon

run:
	make -i -j5 target