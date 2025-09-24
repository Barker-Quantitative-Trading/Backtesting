# Docker Setup

This project sets up a PostgreSQL database along with an optional pgAdmin web interface using Docker Compose.

## Services

### 1. PostgreSQL
- **Container Name:** `market_db`
- **Image:** `postgres:15`
- **Environment Variables:**
  - `POSTGRES_USER=devuser`
  - `POSTGRES_PASSWORD=devpass`
  - `POSTGRES_DB=market_data`
- **Ports:** `5432:5432`
- **Volumes:** `pgdata:/var/lib/postgresql/data` (to persist database data)
- **Notes:**

### 2. pgAdmin (Optional)
- **Container Name:** `pgadmin`
- **Image:** `dpage/pgadmin4`
- **Environment Variables:**
  - `PGADMIN_DEFAULT_EMAIL=admin@admin.com`
  - `PGADMIN_DEFAULT_PASSWORD=admin`
- **Ports:** `8080:80`
- **Depends on:** `postgres` service
- **Notes:**  
  - Access pgAdmin at [http://localhost:8080](http://localhost:8080)  
  - Add the PostgreSQL server in pgAdmin with host: `db` (container network) or `localhost` (from host machine), port `5432`.

## Volumes
- **pgdata:** Persists PostgreSQL data across container restarts.

## Usage

-- **Start services**  
```bash
docker-compose up -d
```

-- **Stop services**  
```bash
docker-compose down
```

-- **Logs**  
```bash
docker-compose logs -f
```