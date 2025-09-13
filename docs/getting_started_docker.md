This doc is mainly for collin to remember what he did as no one else should need to do this   
It will only be mac instructions
---
**Install / start colima**
(this is so that i dont have to use docker desktop)
```bash
brew install colima 
colima start

docker ps
docker-compose up -d
```
("docker-compse" being the name of .yml file) . 

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



