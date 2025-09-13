**This doc is mainly for collin to remember how to set up and transer postgres to docker when the final system is up, no one else should need to do this**   
**These instructions will only be for mac**

Install / start colima  
---
(this is so that i dont have to use docker desktop)
```bash
brew install colima 
colima start

docker ps
docker-compose up -d
```
("docker ps" will list the running docker containers)
("docker-compse" being the name of .yml file) 

Current .yml file in use
---
```yml
services:
  db:
    image: postgres:15
    container_name: market_db
    restart: unless-stopped
    environment:
      POSTGRES_USER: devuser
      POSTGRES_PASSWORD: devpass
      POSTGRES_DB: market_data
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
   pgdata:
```

Using the docker to run postgres
---


```bash
docker exec -it market_db psql -U devuser -d market_data
```
- -it = interactive terminal
- psql is the PostgreSQL CLI client
- connecting to the market_data database as user devuser


Transfering postgres db into docker
---
**Dump existing DB**
```bash
pg_dump -U <your_user> -d <your_db> -F c -b -v -f <name_of_dump_file>.dump   
```
- -F c = custom format (compressed)
- -b = include large objects
- -v = verbose

**Copy it into the container and restore**
```bash
docker cp market_data.dump market_db:/market_data.dump
docker exec -i market_db pg_restore \
  --username=devuser \
  --dbname=market_data \
  --no-owner < market_data.dump
```
(flags to get around having a different Postgres user)

To Res


If you **fail a restore** you can remove it and try again using:
----
```bash
# Stop and remove the container
docker-compose down

# Remove the volume (deletes all DB data)
docker volume rm $(docker volume ls -q | grep pgdata)

# Start fresh container
docker-compose up -d
```


