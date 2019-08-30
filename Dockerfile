FROM node:8.16.1-alpine

WORKDIR /app
ADD backend.js .
ADD package.json .

RUN npm install 
ENTRYPOINT npm start
