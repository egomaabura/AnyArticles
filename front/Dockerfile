FROM node:20-alpine

WORKDIR /workspace/front

COPY ./package.json ./package-lock.json /

RUN npm install

COPY . .
RUN npm run build