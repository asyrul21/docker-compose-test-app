FROM node:14
WORKDIR /usr/src/express-backend
COPY . .
COPY package.json .
COPY package-lock.json .
RUN npm install
RUN npm install -g nodemon
EXPOSE 3000
CMD [ "nodemon", "server.js" ]