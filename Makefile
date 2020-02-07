install_dependencies:
	pip install -r requirements.txt

init_db:
	flask init-db

start:
	flask run

start_heroku:
	gunicorn "pycmicserver:create_app()" --bind 0.0.0.0:${PORT}

test:
	python -m pytest

install: install_dependencies init_db
	mkdir -p instance
	cp pycmicserver/config_example.py instance/config.py

build_docker:
	docker build --tag pycmic-server .

start_vm:
	vagrant up

azure_up:
	cd despliegue
	vagrant box add azure-dummy https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure
	vagrant plugin install vagrant-azure
	vagrant plugin install vagrant-env
	vagrant up
	vagrant ssh-config


