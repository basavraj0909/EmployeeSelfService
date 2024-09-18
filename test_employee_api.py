import requests
from faker import Faker

# Initialize Faker
faker = Faker()

# Define the base URL for your API
BASE_URL = "http://localhost:8000/employees/"

def test_create_employee():
    """
    Creates a single employee using Faker to generate fake data.

    The function makes a POST request to the employee API endpoint,
    sending a JSON payload with fake username, email, phone number,
    and password data. The email and phone number are truncated to
    meet specific field length requirements.

    Prints:
        - A success message with the created employee's details if the
          employee is created successfully (HTTP 201).
        - An error message with the response status code and text if
          the employee creation fails.
    """
    email = faker.email()[:20]  # Ensure email length doesn't exceed 20 characters
    data = {
        "username": faker.user_name(),
        "email": email,
        "phone_number": faker.phone_number()[:15],  # Truncate phone number
        "password": faker.password()
    }
    response = requests.post(BASE_URL, json=data)

    if response.status_code == 201:
        print(f"Employee created successfully: {response.json()}")
    else:
        print(f"Failed to create employee: {response.status_code}, {response.text}")


def test_create_multiple_employees(n):
    """
    Creates multiple employees by calling the `test_create_employee` function n times.

    Args:
        n (int): The number of employees to create.
    """
    for _ in range(n):
        test_create_employee()


def test_get_employees(emp_id=None, page=1):
    """
    Retrieves employee details from the API.

    If an employee ID is provided, retrieves the details of the specific employee.
    If no employee ID is provided, retrieves a paginated list of employees.

    Args:
        emp_id (int, optional): The ID of the employee to retrieve. Defaults to None.
        page (int, optional): The page number for paginated results. Defaults to 1.

    Returns:
        dict: The JSON response from the server if the request is successful.
        None: If the request fails.

    Prints:
        - A success message with the retrieved employee(s) data if the request is successful (HTTP 200).
        - An error message with the response status code and text if the request fails.
    """
    if emp_id:
        # Retrieve details for a specific employee by ID
        response = requests.get(BASE_URL + str(emp_id))
    else:
        # Retrieve a paginated list of employees
        params = {'page': page}
        response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"Page {page} - Employees retrieved successfully: {data}")
        return data
    else:
        print(f"Failed to retrieve employees: {response.status_code}, {response.text}")
        return None


def test_delete_employee(employee_id):
    """
    Deletes an employee by sending a DELETE request to the employee API endpoint.

    Args:
        employee_id (int): The ID of the employee to delete.

    Prints:
        - A success message if the employee is deleted successfully (HTTP 204).
        - An error message with the response status code and text if the deletion fails.
    """
    response = requests.delete(f"{BASE_URL}{employee_id}/")

    if response.status_code == 204:
        print(f"Employee deleted successfully")
    else:
        print(f"Failed to delete employee: {response.status_code}, {response.text}")


if __name__ == "__main__":
    pass
# Create one employee
# test_create_employee()

# Create multiple employees (500 in this case)
# test_create_multiple_employees(500)

# Delete an employee with ID 28
# test_delete_employee(28)

# Retrieve employees (with pagination, defaulting to page 1)
# test_get_employees()
