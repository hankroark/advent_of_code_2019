# Use the official Python 3 image.
# https://hub.docker.com/_/python
#
# python:3 builds a 954 MB image - 342.3 MB in Google Container Registry
# FROM python:3
#
# python:3-slim builds a 162 MB image - 51.6 MB in Google Container Registry
# FROM python:3-slim
#
# python:3-alpine builds a 97 MB image - 33.2 MB in Google Container Registry
FROM python:3-alpine

# Set the working directory to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install ptvsd for debugging
RUN pip install ptvsd

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Run app.py when the container launches
ENTRYPOINT ["python", "-m", "ptvsd", "--port", "3000", "--host", "0.0.0.0", "app.py"]


# RUN apt-get update -y
# RUN apt-get install -y python-pip
#COPY .. /app

# Create and change to the app directory.
#WORKDIR /app

#RUN pip install --no-cache-dir -r requirements.txt

#RUN chmod 444 app.py
#RUN chmod 444 requirements.txt

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
#ENV PORT 8080

# Run the web service on container startup.
#CMD [ "python", "app.py" ]