### 1. Environment

1. For docker

    ```
    Docker version 24.0.2
    ```

1. For local dev

    ```
    Database: postgres:15.2
    Python 3.11
    ```

### 2. Getting started

1. Start services with Docker

    ```
    docker-compose up -d
    ```

1. Dump example data (**_optional_**)

    ```
    docker-compose exec blog-server python manage.py loaddata initial_articles.json
    ```

1. Create a super user (Email: `admin@gmail.com` && password: `super_password`)

    ```
    docker-compose exec blog-server bash createSuperuser.sh
    ```

1. Test the API on **http://127.0.0.1:8000/api/docs**
