# Project Title: Scrapy Test Project

## Project Description
This project is a web scraping application built using **Scrapy** that collects data from websites and stores it in a **PostgreSQL** database. It is containerized using **Docker** for ease of deployment and management. The project structure includes services for running the Scrapy crawler and a PostgreSQL database. Additionally, there is support for running tests using **pytest**.

## Table of Contents
- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Services](#services)
- [Database Setup](#database-setup)
- [Running the Scrapy Crawler](#running-the-scrapy-crawler)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used
- **Scrapy** for web scraping
- **PostgreSQL** for data storage
- **Docker & Docker Compose** for container orchestration
- **pytest** for testing
- **Python** for application code

## Getting Started
These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- **Docker**: Ensure Docker is installed on your machine. You can download it from [Docker’s official site](https://www.docker.com/).
- **Docker Compose**: Ensure Docker Compose is installed. It usually comes bundled with Docker Desktop.

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/username/scrapy_test_project.git
   cd scrapy_test_project
   ```
2. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

## Project Structure
```plaintext
scrapy_test_project/
|-- docker-compose.yml
|-- Dockerfile
|-- requirements.txt
|-- scrapy.cfg
|-- project/
    |-- spiders/
    |-- pipelines.py
    |-- settings.py
|-- tests/
    |-- test_spiders.py
```

- **docker-compose.yml**: Configuration file for defining services.
- **Dockerfile**: Instructions for building the Scrapy application container.
- **requirements.txt**: Lists Python dependencies.
- **project/**: Contains the Scrapy project code and configurations.
- **tests/**: Contains test cases for the application.

## Services
The project is composed of the following services:

### PostgreSQL Service
- **Image**: `postgres:15`
- **Container Name**: `postgres_db`
- **Environment Variables**:
  - `POSTGRES_USER`: `scrapy_user`
  - `POSTGRES_PASSWORD`: `scrapy_password`
  - `POSTGRES_DB`: `scrapy_db`
- **Ports**: `5432:5432`
- **Volume**: `postgres_data:/var/lib/postgresql/data`

### Scrapy Service
- **Build Context**: `.`
- **Dockerfile**: `Dockerfile`
- **Container Name**: `scrapy_app`
- **Depends On**: `postgres`
- **Environment Variables**:
  - `DATABASE_URL`: `postgresql+psycopg2://scrapy_user:scrapy_password@postgres:5432/scrapy_db`
- **Volume**: `.:/usr/src/app`
- **Command**: `scrapy crawl trip`



## Database Setup
The PostgreSQL database will automatically be initialized with the user and database specified in the environment variables.

## Running the Scrapy Crawler
To start the Scrapy crawler:
```bash
docker-compose up scrapy
```

## Testing
To include testing, add the `pytest` service:
```bash
   pip install pytest pytest-cov
```

Alternatively, you can run tests locally:
```bash
pytest --cov=testproject tests/
```

## Contributing
Feel free to submit pull requests and report issues. Contributions are welcome!

