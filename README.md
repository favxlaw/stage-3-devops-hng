# Messaging System with FastAPI, RabbitMQ, Celery, and Nginx

## Overview

This project demonstrates the setup of a messaging system using FastAPI for the web framework, RabbitMQ as the message broker, Celery for task queue management, and Nginx as a reverse proxy. The system includes endpoints for sending emails and logging messages asynchronously.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Application](#running-the-application)
5. [Nginx Setup](#nginx-setup)
6. [Exposing the Endpoint using Ngrok](#exposing-the-endpoint-using-ngrok)


## Project Structure

.
├── app
│ ├── init.py
│ ├── main.py
│ └── tasks.py
├── requirements.txt
├── nginx.conf
└── README.md

markdown
Copy code

- `app/__init__.py`: Initializes the app module.
- `app/main.py`: Contains the FastAPI application and endpoints.
- `app/tasks.py`: Defines the Celery tasks.
- `requirements.txt`: Lists the Python dependencies.
- `nginx.conf`: Nginx configuration file.
- `README.md`: Project documentation.

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Set up a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install RabbitMQ**:
    - For Ubuntu:
        ```bash
        sudo apt-get install rabbitmq-server
        sudo systemctl enable rabbitmq-server
        sudo systemctl start rabbitmq-server
        ```

## Configuration

Create a `.env` file in the root directory and add the following configuration:

```env
CELERY_BROKER_URL=amqp://localhost
CELERY_RESULT_BACKEND=rpc://
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
SMTP_USERNAME=your_email@example.com
SMTP_PASSWORD=your_password
Running the Application
Start the Celery worker:

celery -A app.tasks worker --loglevel=info
Run the FastAPI application:


uvicorn app.main:app --host 0.0.0.0 --port 8000
Nginx Setup
Install Nginx:

sudo apt-get install nginx
Configure Nginx:
Edit the nginx.conf file with the following content:


sudo apt-get install ngrok
Expose your local server:

ngrok http 8000
Get the public URL:


HNG internship
