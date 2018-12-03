This is a containerized server which listens for an HTTP request to the root URL, determines whether the UTC time is 11:11, and responds to the client with HTML that says whether the time is 11:11.

To run the application:
  - Install Docker on your local machine
  - Start your Docker daemon: `$ dockerd`
  - Clone the application to your local machine: `git clone https://github.com/nickedwards109/is-it-eleven-eleven.git`
  - Navigate to the application's root directory
  - Build an image of the server and its dependencies (in this case, labeling the image with the tag 'server'): `$ docker build -t server .`
  - Run a container as a runtime instance of the image, and map port 4000 on your local host to the server's port 80: `$ docker run -p 4000:80 server`
  - Visit http://localhost:4000 in a browser!
