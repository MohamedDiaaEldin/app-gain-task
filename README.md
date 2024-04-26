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

***- Local Access*** : Open Postman Collection and go to local folder [postman collection](./appgain-task.postman_collection.json) in order to use the API

***- Online Access*** deployed on Render: You can access the API at the following URL:
[API Endpoint](https://app-gain-task.onrender.com/).  Open Postman Collection and go to production folder [postman collection](./appgain-task.postman_collection.json) 



# Flask App API Documentation

## Endpoints

### 1. /register (POST)

Registers a new user with the provided information.

#### Request Body
```json
{
    "username": "string",
    "email": "string",
    "address": "string",
    "password": "string"
}
```
#### Responses
- 409 Conflict: If a user with the provided email already exists.
- 200 OK: If the registration is successful.
- 500 Internal Server Error: If a server error occurs.

### 2. /login (POST)
Logs in a user with the provided credentials and sets an access token in the cookies.


#### Request Body
```json
{
    "email": "string",
    "password": "string"
}
```
#### Responses
- 404 Not Found: If the user with the provided email is not found.
- 401 Unauthorized: If the provided password is incorrect.
- 200 OK: If the login is successful.
- 500 Internal Server Error: If a server error occurs.

### 3. /order (POST)
Places an order for a product with the provided information.


#### Request Body
```json
{
    "product_id": 656,
    "quantity": 2,
    "card_number": 45656464655,
    "exp_date": "11/25",
    "csv": 987
}
```
#### Responses
- 404 Not Found: If the product is not found or the quantity is not available.
- 401 Unauthorized: If the user is deleted from the database . 
- 500 Internal Server Error: If there are issues with the payment server or our backend.
- 200 OK: If the order is successfully placed.

### 4. /logout (GET)
Deletes Access Token from the Cookies 


### EndPoint Usage 
- Check [postman collection](./appgain-task.postman_collection.json)







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

