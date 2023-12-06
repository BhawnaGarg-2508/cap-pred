# Use the official Python image as the base image
FROM python:3.9.13

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 5000 (change the port if your Flask app runs on a different port)
EXPOSE 5000

# Define the command to run your application
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:3000"]



