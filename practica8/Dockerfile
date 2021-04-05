FROM node:current-slim

WORKDIR C:\\Users\\Moino\\Documents\\1er2021\\sa\\lab\\practica8

COPY package.json .

RUN npm install

RUN npm install express mysql   --save

EXPOSE 3000

CMD ["npm","run","start"]

COPY . .