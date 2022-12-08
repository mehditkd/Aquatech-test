cp schema/create.sql docker/db/docker-entrypoint-initdb.d/create.sql
cp -r site/backend/ docker/api/src
cp -r site/frontend docker/front/src
cd docker
sudo docker-compose build && sudo docker-compose down && sudo docker-compose up