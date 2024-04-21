# Content Management Service Documentation

## Overview
This documentation provides an overview of the components, Docker configurations, and FastAPI endpoints implemented in the `content_mgmt_service` for the BQP Assignment Check platform. The service is designed to manage content creation, update, and retrieval processes in a scalable and efficient manner.

## Directory Structure

    /content_mgmt_service
    ├── /compose
    │   └── /local
    │       ├── Dockerfile
    │       └── start
    ├── /src
    │   ├── database.py              # Defines database configurations and ORM models
    │   ├── main.py                  # Entry point for the FastAPI application
    │   ├── requirements.txt         # Lists all Python dependencies
    │   ├── utils.py                 # Contains utility classes and functions
    │   └── /config
    │       ├── constants.py         # Stores constant values used throughout the application
    │       └── .env                 # Environment variables configuration
    └── local.yml                    # Docker Compose file for local development

## Components

### Docker Configuration
- **File**: `local.yml`
- **Description**: Configures the Docker environment for the content management service, setting up service parameters, exposed ports, and volume mappings.

### Dockerfile
- **Location**: `compose/local/Dockerfile`
- **Description**: Defines the steps to build the Docker image for the content management service, including the installation of Python packages and setup commands.

### Startup Script
- **File**: `compose/local/start`
- **Description**: A bash script to start the FastAPI server with Uvicorn, specifying the host, port, and reload configuration.

## Source Code Files

### Main Application (FastAPI)
- **File**: `src/main.py`
- **Description**: Implements the FastAPI application, defining routes for managing articles, including CRUD operations and user interactions.

### Database Configuration
- **File**: `src/database.py`
- **Description**: Sets up the database connection using SQLAlchemy, defines the ORM models for articles, and handles session creation.

### Utility Functions
- **File**: `src/utils.py`
- **Description**: Provides utility functions and classes such as `NotifierClient` for sending notifications and `UserProfileClient` for fetching user profiles.

### Python Requirements
- **File**: `src/requirements.txt`
- **Description**: Lists all necessary Python packages required to run the content management service.

## Configuration Files

### Environment Variables
- **File**: `src/config/.env`
- **Content**:
    ```
    GOOGLE_CLIENT_ID="..."
    GOOGLE_CLIENT_SECRET="..."
    GOOGLE_REDIRECT_URI="..."
    ```

### Constants
- **File**: `src/config/constants.py`
- **Description**: Optionally used to define constant values that are utilized throughout the application.

## Setup and Deployment
To deploy the content management service locally using Docker:
1. Navigate to the service directory:
    ```bash
    cd /path/to/content_mgmt_service
    ```
2. Build and run the Docker container:
    ```bash
    docker-compose -f local.yml up --build
    ```

This setup ensures the content management service is properly configured and ready for integration with other services in the BQP Assignment Check platform.
