# Step 1: Use the official Python Docker image as the base
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy requirements.txt to the container
COPY requirements.txt /app/

# Step 4: Install the Python dependencies (libraries)
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the project files into the container
COPY . /app/

# Step 6: Expose the Django default port (8000)
EXPOSE 8000

# Step 7: Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
