install_dependencies:
	pip install -r requirements.txt

init_db:
	flask init-db

start:
	flask run

test:
	python -m pytest

install: install_dependencies init_db
	mkdir -p instance
	cp pycmicserver/config_example.py instance/config.py


