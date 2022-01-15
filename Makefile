db_create:
	python3 src/create_db.py

db_migrate:
	python3 migrate.py

db_fill_cities:
	python3 src/dbpart/fill_cities_db.py

db_prepare:
	make db_create
	make db_migrate

requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

conn_psql_docker_psql:
	sudo docker exec -ti postgres psql --u postgres

docker_build_image:
	sudo docker build . -t bystrovmikhail/carholder:latest

docker_create_network:
	bash bin/postgres_net.sh

docker_run_migrations:
	sudo docker-compose run carholder make db_prepare

docker_run_bot:
	sudo docker-compose run carholder python3 main.py
