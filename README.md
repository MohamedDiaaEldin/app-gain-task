# Flask App README

## Introduction
This Flask application serves as a backend for managing user authentication (signup, login, logout) and provides an endpoint for placing orders. Additionally, it includes functionality to send email notifications with order details upon successful placement.

## Installation
1. **Clone the repository:**
git clone https://github.com/MohamedDiaaEldin/app-gian-task.git

2. **Create virtual environment:**
- ```
    python3 -m venv myenv
  ```

3. **Activate the virtual environment:**
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. **Navigate to App Folder:**
    ```
    cd app
    ```
5. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```
5. **Create Environment File:**
    create .env file with these variables
    ```
    DATABASE_URL=database url
    JWT_SECRET=app secret
    EMAIL=email server
    PASSWORD=password of email server.
    ```
6. **Run DataBase Using Postgres Docker Image:**
    ```
    chmod +x ./scripts/run_database.sh
    ./scripts/run_database.sh
    
   ```
7. **Define App Variable:**
    ```
    export FLASK_APP=main
    ```
8. **Add Initial Data:**
    ```
    python3 add_data.py
    ```

9. **Run Migration:**
    ```
    flask db upgrade
    ```
## Usage
1. **Run the application:**
    ```
    python3 app.py
    ```



2. **Access the application:**
Open a web browser and go to [http://localhost:5000](http://localhost:5000)

## Docker
You can also run this Flask application using Docker.

1. **Clone Docker Hub Registry:**
    https://hub.docker.com/repository/docker/mohameddiaaeldin/app-gain-task

2. **Run Docker Image**
    ```
    docker run -p 5000:5000 --net="host" app-gain-image
    ```
## Structure
The project structure is organized as follows:
- **main.py**: Main Flask application file.
- **models/**: database models.
- **middlewares/**: Middleware components for processing requests before they hit the endpoint.
- **controllers**:  Controller modules for handling requests and generating responses.
- **Utilities**: Utility modules for common functionalities..
- **migration**: Migration files for managing database schema changes..
- **scripts**: Bash scripts for automation or setup tasks..
- **database.py**: database config.
- **Dockerfile**: Docker configuration file for containerization..
- **requirements.txt**: List of Python dependencies.
- **add_data.txt**: Initial data for pre-populating the database..
- **appgain-task.postman_collection.json**: Postman collection containing endpoints.

