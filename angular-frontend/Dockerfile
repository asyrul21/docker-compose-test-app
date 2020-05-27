FROM node:14
WORKDIR /usr/src/angular-frontend
COPY . .
COPY package.json .
COPY package-lock.json .
RUN npm install
RUN npm install -g nodemon
EXPOSE 4200
CMD [ "npm", "start" ]