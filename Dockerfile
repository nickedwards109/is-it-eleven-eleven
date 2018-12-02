# Use Python 3.7 runtime as a parent image
FROM python:3.7-slim

# Set the working directory
WORKDIR server

# Copy the current directory contents into the container
COPY . /server

# Install the dependencies specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the server when the container launches
CMD ["python", "server.py"]]
