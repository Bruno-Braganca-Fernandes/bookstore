# Bookstore

[![Build Status](https://github.com/Bruno-Braganca-Fernandes/bookstore/actions/workflows/build.yml/badge.svg)](https://github.com/Bruno-Braganca-Fernandes/bookstore/actions/workflows/build.yml)
[![PR Check Status](https://github.com/Bruno-Braganca-Fernandes/bookstore/actions/workflows/workflow-pr.yml/badge.svg)](https://github.com/Bruno-Braganca-Fernandes/bookstore/actions/workflows/workflow-pr.yml)
[![Deploy Status](https://github.com/Bruno-Braganca-Fernandes/bookstore/actions/workflows/deploy.yml/badge.svg)](https://github.com/Bruno-Braganca-Fernandes/bookstore/actions/workflows/deploy.yml)

A modern Bookstore REST API built with Django and Python 3.13. Originally inspired by the EBAC Full Stack Python course, this project was independently refactored, updated, and enhanced to meet current industry standards, including a fully automated CI/CD pipeline.

## Prerequisites

- Python 3.13+
- Poetry
- Docker & docker-compose

## Quickstart

1. Clone this project:

   ```shell
   git clone [https://github.com/Bruno-Braganca-Fernandes/bookstore.git](https://github.com/Bruno-Braganca-Fernandes/bookstore.git)

2. Install dependencies:
   
   ```shell
   cd bookstore
   poetry install

3. Run the local dev server:

   ```shell
   poetry run python manage.py migrate
   poetry run python manage.py runserver

4. Run the Docker dev server environment:

   ```shell
   docker-compose up -d --build
   docker-compose exec web python manage.py migrate

5. Run tests inside Docker:

    ```shell
    docker-compose exec web python manage.py test
    ```

## CI/CD & Deployment

This project uses **GitHub Actions** for Continuous Integration (CI) and Continuous Delivery (CD).
- **CI:** Automatically runs formatting checks (Wemake Python Styleguide) and unit tests on Pull Requests.
- **CD:** Automatically deploys the application to **PythonAnywhere** when code is merged into the `main` branch. Static files are handled by **WhiteNoise**.
