install_dependencies:
	pip install -r requirements.txt

init_db:
	flask init-db

start:
	flask run

test:
	python -m pytest

install: install_dependencies init_db



