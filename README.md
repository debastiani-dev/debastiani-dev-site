# debastiani-dev-site

Institutional Website & Portfolio Management System for the company debastiani.dev

## 🚀 Tech Stack

- **Framework**: Django 5.2+ (Python 3.12+)
- **Database**: PostgreSQL 17
- **Dependency Management**: Poetry
- **Environment**: Docker & Docker Compose
- **Testing**: Pytest & Pytest-Cov
- **Code Quality**: Black, Isort, Flake8, Mypy, Pylint, Pre-commit

## 📋 Prerequisites

Ensure you have the following installed on your local machine:
- [Docker](https://docs.docker.com/get-docker/) and Docker Compose
- [Poetry](https://python-poetry.org/docs/#installation)
- [Make](https://www.gnu.org/software/make/)

## 🛠️ Local Development Setup

This project uses a `Makefile` to simplify development workflows. The development environment runs entirely within Docker containers.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/debastiani-dev/debastiani-dev-site.git
   cd debastiani-dev-site
   ```

2. **Set up Environment Variables**:
   Copy the example environment file and adjust it if necessary.
   ```bash
   cp .env.example .env
   ```

3. **Start the Development Environment**:
   This command verifies dependencies, creates the Docker network, and starts the web and database containers in detached mode.
   ```bash
   make dev/up-d
   ```

4. **Apply Database Migrations**:
   ```bash
   make dev/migrate
   ```

5. **Create a Superuser**:
   To access the Django Admin panel at `/admin/`.
   ```bash
   make dev/create-admin
   ```
   *Note: The default credentials created are `admin@example.com` / `admin`.*

6. **Access the Application**:
   - Website: [http://localhost:8000](http://localhost:8000)
   - Admin Panel: [http://localhost:8000/admin](http://localhost:8000/admin)

7. **Stop the Development Environment**:
   ```bash
   make dev/down
   ```

## 🧪 Testing

The project uses `pytest` for testing. Tests are run inside an isolated test database container using `docker-compose.test.yml`.

- **Run all tests**:
  ```bash
  make pytest
  ```
- **Run tests with coverage report**:
  ```bash
  make pytest-cov
  ```

## 🧹 Code Quality & Linting

We enforce strict code quality using a suite of formatters and linters.

- **Format Code** (Runs autoflake8, isort, black):
  ```bash
  make format
  ```
- **Lint Code** (Runs isort check, black check, flake8, mypy, pylint):
  ```bash
  make lint
  ```
- **Run Pre-Commit Hooks Manually**:
  ```bash
  make run-pre-commit-hook
  ```

## 📚 Makefile Reference

Here are the most commonly used `make` commands:

| Command | Description |
|---|---|
| `make help` | Show all available commands |
| `make dev/up-d` | Start the local development environment in detached mode |
| `make dev/down` | Stop and remove development containers, networks, and volumes |
| `make dev/logs` | View and tail the logs of the running containers |
| `make dev/makemigrations` | Generate new database migrations |
| `make dev/migrate` | Apply database migrations |
| `make dev/startapp app=<name>` | Create a new Django app inside the `apps/` directory |
| `make dev/create-admin` | Create a default superuser for the admin panel |
| `make format` | Automatically format all Python code |
| `make lint` | Run all linters and static type checks |
| `make pytest` | Run the test suite |
| `make pytest-cov` | Run the test suite and generate a coverage report |

## 🏗️ Project Structure

- `apps/`: Contains all custom Django applications (e.g., `base`, `pages`, `portfolio`, `users`).
- `core/`: Django core configuration (`settings.py`, `urls.py`, `wsgi.py`, etc.).
- `static/`: Static assets like CSS, JS, and images.
- `templates/`: Global HTML templates.
- `tests/`: Automated tests structured to mirror the `apps/` directory.
