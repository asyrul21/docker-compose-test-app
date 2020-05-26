# Multi-Container Docker Compose Demo
This app is to demonstrate how to use docker compose to integrate multiple docker containers of varying languages : python and javascript

## Docker Setup
1. Pull latest Python image
```bash
docker pull python
```

## The Spacy API
1. Create your Flask-resful app, specifiying the port number
```python
if __name__ == '__main__':
    app.run(debug=True, port=80)
```

2. Create Dockerfile (remove comments)
```Dockerfile
# select python image
FROM python:3

# specify workinf directory
# WORKDIR WORKDIR /usr/src/spacyapi

#copy all code to dir in container
COPY . .

# copy requirements.txt
COPY requirements.txt requirements.txt

# install dependencies
RUN pip install -r requirements.txt

# run command
CMD ["python", "app.py"]
```

3. Check to see docker works with app
```bash
# build docker image
docker build -t "spacy.api" .
# --> Successfully built df3751a3cfa2

# view all images
docker images

# run image as container
docker run -d -p 56733:80 --name="spacy.py"
# -p takes port mapping <host port>:<container port>

# view all running containers
docker ps
```

4. API call from host would be:
localhost:56733/GetVector/?sentence=hello

5. Clean up docker images
https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes

- run all wanted containers and images

- run
```bash
docker system prune
```

## The Express Backend

https://nodejs.org/fr/docs/guides/nodejs-docker-webapp/

1. Create your express app. Test spacyAPI call using 
localhost:56733/GetVector/?sentence=hello

2. Build Dockerfile
```Dockerfile
# node image
FROM node:14

# copy source code
COPY . .

# copy package.json and package-lock.json
COPY package*.json ./

# install dependencies
RUN npm install

# expose container to port
EXPOSE 8080

# run command
CMD [ "node", "server.js" ]
```

3. Create .Dockerignore file
```dockerignore
node_modules
npm-debug.log
```

4. Check to see docker works with app
```bash
# build docker image
docker build -t "express.backend" .
# --> Successfully built df3751a3cfa2

# view all images
docker images

# run image as container
docker run -d -p 49160:3000 --name="express.backend" "express.backend"

# view all running containers
docker ps
```

5. API Call:
localhost:49160/vectorfor/?word=hello

NOTE: this wont work because each container is independent on each other


## The Docker Compose file
1. Create docker-compose.yml
```yml
version: '3.2'

services:
  spacy-vector-api:
    # dockerfile path
    build: ./spacy-vector-api
    # binding to volume
    volumes: 
      - './spacy-vector-api:/usr/src/app'
    # port mapping
    ports:
      - 5001:80

  express-backend:
    # dockerfile path
    build: ./express-backend
    # binding to volume
    volumes: 
      - './express-backend:/usr/src/app'
    # port mapping
    ports:
      - 5000:3000
    depends_on:
      - spacy-vector-api
```

2. Some useful docker-compose commands
```bash
docker-compose up
docker-compose down -v
docker-compose up -d --force-recreate
docker-compose up --build --force-recreate
```


## References

https://docs.docker.com/compose/gettingstarted/

https://www.youtube.com/watch?v=Qw9zlE3t8Ko

https://thinkwhere.com/multi-container-deployment-with-docker-compose/

https://www.digitalocean.com/community/tutorials/workflow-multiple-containers-docker-compose

https://docs.microsoft.com/en-us/dotnet/architecture/microservices/multi-container-microservice-net-applications/multi-container-applications-docker-compose

https://stackoverflow.com/questions/18497688/run-a-docker-image-as-a-container

https://stackoverflow.com/questions/30323224/deploying-a-minimal-flask-app-in-docker-server-connection-issues