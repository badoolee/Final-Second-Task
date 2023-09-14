# Simple User REST API

This is a User simple REST API that allows you to perform CRUD (Create, Read, Update, Delete) operations on a user details.

# Table of Contents
- Setup And Installation
- Running The Application
- Usage
  - Creating a New User
  - Fetching User Details
  - Modifying User Details
  - Removing a User

## Setup And Installation

1. Clone this repository to your local machine:

   **git clone** [repository-url]

2. Create a virtual environment and activate it:
    First ensure that python is installed in your computer then create a virtual environment by pressing control+shift+p on your keyboard and select python environment. create the virtual environment with the lastest version of python on your PC e.g python version 3.11.0.

3. Before you proceed, make sure you have the following packages are installed:

    - Flask
    - Flask-SQLAlchemy
    - flask-smorest
    - marshmellow
    - gunicorn
    - Your chosen database (SQLite)

    Install the above packages by:

    **pip install -r requirements.txt**

4. Initialize the database and create the necessary tables:

    The database will be automatically created in an instance folder(**data.db**) when you run the application

## Running The Application
To run the Flask app, double click on the **app.py** in the folder and select run **Run Python File On Terminal** 

## Usage

1. Creating a new user:
    To add a new user, send a POST request to the /api endpoint with a JSON payload containing the person's name, occupation and location.

    Example:
    POST [http://127.0.0.1:5000/api]

    REQUEST:
    ```
    {
	"name": "John Wick",
    "occupation: "Hitler",
    "location: "U.S.A"
    }
    ```
    RESPONSE:
    ```
    {
    "id": 1,
    "name": "John Wick",
    "occupation: "Hitler",
    "location: "U.S.A"
    }
    ```
2. Fetching User Details:
    To fetch details of a user, send a GET request to the /api/<user_id> endpoint, where <user_id> is the ID of the person you want to retrieve.

    Example:
    GET [http://127.0.0.1:5000/api/1]

    RESPONSE:
     ```
    {
    "id": 1,
    "name": "John Wick",
    "occupation: "Hitler",
    "location: "U.S.A"
    }
    ```
3. Modifying User Details:
    To modify the details of an existing user, send a PUT request to the /api/<user_id> endpoint with a JSON payload containing the updated information.

    Example:
    PUT [http://127.0.0.1:5000/api/1]

    REQUEST:
    ```
    {
    "occupation: "Banker",
    "location: "Canada"
    }

    RESPONSE:
     ```
    {
    "id": 1,
    "name": "John Wick",
    "occupation: "Banker",
    "location: "Canada"
    }
    ```

4. Removing a User:
    To remove a user, send a DELETE request to the /api/<user_id> endpoint, where <user_id> is the ID of the person you want to delete.

    Example:
    Delete [http://127.0.0.1:5000/api/1]

    RESPONSE:
     ```
    {
    "message": "The User details is deleted Successfully",
    }
    ```

