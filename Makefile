install_dependencies:
	pip install -r requirements.txt

init_db:
	FLASK_APP=pycmicserver
	flask init-db

start:
	FLASK_APP=pycmicserver
	flask run

test:
	pytest

install: install_dependencies init_db



