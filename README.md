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
WORKDIR /usr/src/spacyapi

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
COPY package.json .
COPY package-lock.json .

# install dependencies
RUN npm install
RUN npm install -g nodemon

# expose container to port
EXPOSE 3000

# run command
CMD [ "nodemon", "server.js" ]
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

NOTE: this wont work because each container is independent on each other, hence API call from express to localhost:56733/GetVector/?sentence=hello is not  possible. We need to use Docker Compose.


## The Docker Compose file
1. Create docker-compose.yml
```yml
version: '3.3'

services:
  spacy-vector-api:
    # dockerfile path
    build: ./spacy-vector-api
    # binding to volume
    volumes: 
      - type: bind
        source: ./spacy-vector-api
        target: /usr/src/spacyapi
    # port mapping
    ports:
      - 5001:80

  express-backend:
    # dockerfile path
    build: ./express-backend
    # binding to volume
    volumes: 
      - type: bind
        source: ./express-backend
        target: /usr/src/express-backend
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

## The Angular Client

1. Create Angular app using cli
```bash
ng new angular-frontend
```

2. Make sure to delelete git repo within angular app
```bash
rm -rf .git
```

3. Test Api call to Express docker container with (after docker-composing both the spacy api and express apps)
http://localhost:5000/vectorfor/?word=hello

4. Create server.js in root and change package.json start script
- server.js
```javascript
var express = require('express')

app = express()

app.use(express.static('./dist/angular-frontend'));

app.get('/*', function (req, res) {
    res.sendFile('index.html', { root: 'dist/angular-frontend/' }
    );
});

app.listen(process.env.PORT || 4200, function () {
    console.log('Angular server is listening...');
});
```

- package.json
```json
//"start": "ng serve"
"start": "nodemon server.js"

OR

"start": "ng serve --host 0.0.0.0",
```

5. Build to production
```bash
ng build --prod
```

6. Test once again with api call to http://localhost:5000/vectorfor/?word=hello but using
```bash
nodemon server.js
```

7. Create the Dockerfile
```Dockerfile
# get node image
FROM node:14
# change to work directory
WORKDIR /usr/src/angular-frontend
# copy source code in
COPY . .
# copy package.json files
COPY package.json .
COPY package-lock.json .
# install dependencies
RUN npm install
RUN npm install -g nodemon
# expose port
EXPOSE 4200
# start script
CMD [ "npm", "start" ]
```

8. Create Dockerignore file
```dockerignore
node_modules
npm-debug.log
```

9. Check to see docker works with app, although the API call wont work just yet.
```bash
# build docker image
docker build -t "angular.frontend" .

# view all images
docker images

# run image as container
docker run -d -p 4200:4200 --name="angular.frontend" "angular.frontend"

# view all running containers
docker ps

# deletes uneeded images
docker system prune
```

10. Now we can update the docker-compose.yml
```yml
version: '3.3'

services:
  spacy-vector-api:
    build: ./spacy-vector-api
    volumes: 
      - type: bind
        source: ./spacy-vector-api
        target: /usr/src/spacyapi
    ports:
      - 5001:80

  express-backend:
    build: ./express-backend
    volumes: 
      - type: bind
        source: ./express-backend
        target: /usr/src/express-backend
    ports:
      - 5000:3000
    depends_on:
      - spacy-vector-api

    express-backend:
      build: ./angular-frontend
      volumes: 
        - type: bind
          source: ./angular-frontend
          target: /usr/src/angular-frontend
      ports:
        - 4200:4200
      depends_on:
        - spacy-vector-api
        - express-backend
```

11. Api call to express backend can be made by using its host port:
```javascript
var res = this.http.get('http://localhost:5000/vectorfor/?word=' + word);
```

12. The run docker compose up
```bash
docker system prune

# run in background (detached mode)
docker-compose up -d

docker-compose up --build
```


## References

https://docs.docker.com/compose/gettingstarted/

https://www.youtube.com/watch?v=Qw9zlE3t8Ko

https://thinkwhere.com/multi-container-deployment-with-docker-compose/

https://www.digitalocean.com/community/tutorials/workflow-multiple-containers-docker-compose

https://docs.microsoft.com/en-us/dotnet/architecture/microservices/multi-container-microservice-net-applications/multi-container-applications-docker-compose

https://stackoverflow.com/questions/18497688/run-a-docker-image-as-a-container

https://stackoverflow.com/questions/30323224/deploying-a-minimal-flask-app-in-docker-server-connection-issues

https://scotch.io/tutorials/create-a-mean-app-with-angular-2-and-docker-compose

https://stackoverflow.com/questions/52773088/how-can-i-run-angular-using-docker-compose

https://docs.docker.com/config/containers/resource_constraints/