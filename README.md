# Omini Data Collection Service

This project is a Python service that collects data from Omini and saves it to a PostgreSQL database. It uses **Alembic** for database migration management.

## Requirements

- Docker
- Docker Compose

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/larissamato/service-report.git
   cd service-report
   ```

2. Copy the `.env.example` file to `.env` in the project root.

   > **Note:** Change the values as needed for your local setup.

3. Run the command to start the containers:

   ```bash
   docker-compose up --build
   ```

## Project Structure

- **app/**: Contains the Python application.
- **migrations/**: Directory managed by Alembic for database migrations.

## Database Migrations

This project uses Alembic to manage database migrations. Migrations will be applied automatically when the service starts.

If you need to generate new migrations manually, use the commands below:

1. To create a new migration:

   ```bash
   docker-compose exec app alembic revision --autogenerate -m "migration message"
   ```

2. To apply migrations:

   ```bash
   docker-compose exec app alembic upgrade head
   ```

## Stopping the Service

To stop the containers, run:

```bash
docker-compose down
```
