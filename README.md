Commands to build and run docker container:

docker build -t organizations-app-image .

docker run -d --name organizations-app -p 8000:8000 organizations-app-image

API-KEY: secret