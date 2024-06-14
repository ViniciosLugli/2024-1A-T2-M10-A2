# 2024-1A-T2-M10-A2

This project was a API RESTful developed in [Python](https://www.python.org/) using [FastAPI](https://fastapi.tiangolo.com/) to manage blog posts! It was a good example of how to use FastAPI to create a simple API with CRUD operations, [NGINX](https://www.nginx.com/) to serve the API and [Docker](https://www.docker.com/) to containerize the application and make it easier to deploy.

## Features

-   CRUD operations for blog posts (Create, Read, Update and Delete)
-   API RESTful using [FastAPI](https://fastapi.tiangolo.com/)
-   [NGINX](https://www.nginx.com/) to serve the API
-   [Docker](https://www.docker.com/) to containerize the application and manage the services
-   [Insomnia](https://insomnia.rest/) to test the API
-   Well organized project structure with a clear separation of concerns

## How to use

### Requirements

-   [Docker](https://www.docker.com/)
-   [Python](https://www.python.org/)
-   [Git](https://git-scm.com/)

### Setup

1. Clone the repository

    ```bash
    git clone git@github.com:ViniciosLugli/2024-1A-T2-M10-A2.git
    ```

2. Change to the project directory

    ```bash
    cd 2024-1A-T2-M10-A2
    ```

## Running the project

#### Local

1. Go to the API directory

    ```bash
    cd api
    ```

2. Set the virtual environment

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Run the API

    ```bash
    python3 src/main.py
    ```

5. Access the API

    The API will be available at [http://0.0.0.0:3001](http://0.0.0.0:3001)

#### Docker

1. Run the services

    > In the root directory of the project:

    ```bash
    docker compose up --build
    ```

2. Access the API

    The API will be available at [http://0.0.0.0:3000](http://0.0.0.0:3000)

## API Endpoints

You can access the API documentation at [http://0.0.0.0:3000/docs](http://0.0.0.0:3000/docs) on docker or [http://0.0.0.0:3001/docs](http://0.0.0.0:3001/docs) on local.

## Logs

The logs file are located in the [logs/logs.log](logs/logs.log) file. Current logs are commited to the repository for demonstration purposes. based on the demonstration video, the logs are being written to the file.

## Insomnia

You can use [Insomnia](https://insomnia.rest/) to test the API. You can import the [Insomnia](assets/Insomnia.json) file to have all the requests ready to use and test the API!

![insomnia](https://github.com/ViniciosLugli/2024-1A-T2-M10-A2/assets/40807526/602b5f8c-5a81-4f25-a230-6bee1c113fbd)

## Demo of the project using Insomnia

<div align="center">
  <video src="https://github.com/ViniciosLugli/2024-1A-T2-M10-A2/assets/40807526/d26cc7e2-7c96-44cd-ba6d-482eef873594" />
</div>
