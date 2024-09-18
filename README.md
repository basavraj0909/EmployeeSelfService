
# Employee Management API

The Employee Management API is a Django-based REST API designed to manage employee data within an organization. It supports CRUD operations, secure password handling, and custom logging for various operations.

# Features

- **CRUD Operations**: Create, Read, Update, and Delete employee records.
- **Secure Password Handling**: Passwords are hashed and stored securely.
- **Custom Logging**: Logs are generated for various actions (creation, updating, deletion).
- **RESTful API**: JSON-based responses for easy integration with front-end applications.

# Requirements
- Python 3.9+
- Django 3.2+
- Django REST Framework 3.12+

# API Endpoints
- Authentication
    - Register: POST /employees/
        - Request body: { "username": "str", "email": "str",                "phone_number": "str", "password": "str" }
        - Creates a new employee. Password is required and  must be hashed before storage.


# Employee Management

- List Employees: GET /employees/
    - Returns a list of all employees.

- Retrieve Employee: GET /employees/{id}/
    - Returns detailed information about a specific employee by ID.

- Update Employee: PUT /employees/{id}/
    - Request body: { "username": "str", "email": "str", "phone_number": "str", "password": "str" }
    - Updates an existing employee’s information.

- Delete Employee: DELETE /employees/{id}/
    - Deletes an employee record by ID.

# Logging
The API includes custom logging for tracking employee creation, updates, and deletions. Logs are available in the console output.

## API Testing Script

This project includes an API testing script to perform CRUD operations on the employee management API. The script uses the `requests` library and `Faker` to generate test data.

### Script Overview

The testing script provides the following functionalities:

- **Create a single employee**: Generates fake employee data and sends a POST request to create the employee.
- **Create multiple employees**: Generates and sends multiple POST requests to create a specified number of employees.
- **Retrieve employees**: Fetches employee data, either by employee ID or through pagination.
- **Delete an employee**: Deletes an employee based on their ID.

### Usage

Make sure to have the `requests` and `Faker` libraries installed before running the script:

```bash
pip install requests faker
