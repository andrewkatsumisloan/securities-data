FROM node:14.17.3-buster

WORKDIR /client

EXPOSE 3000

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm install --legacy-peer-deps

COPY . .

CMD ["npm","run","start"]
