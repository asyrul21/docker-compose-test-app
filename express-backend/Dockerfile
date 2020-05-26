FROM node:14
WORKDIR /usr/src/express-backend
COPY . .
COPY package.json .
COPY package-lock.json .
RUN npm install
EXPOSE 3000
CMD [ "node", "server.js" ]