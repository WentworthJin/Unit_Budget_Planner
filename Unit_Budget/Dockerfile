FROM node:9
RUN mkdir /Unit_Budget

WORKDIR /Unit_Budget

COPY ./package.json /Unit_Budget/package.json
COPY ./package-lock.json /Unit_Budget/package-lock.json

pip3 install -r ./Python_File/requirements.txt

RUN npm install --silent

## import the source code into the docker Unit budget
COPY ./src /Unit_Budget/src

COPY ./dist /Unit_Budget/dist

COPY ./Python_File /Unit_Budget/Python_File

RUN pip3 install -r /Unit_Budget/Python_File/requirements.txt

COPY ./preload.js /Unit_Budget/preload.js
COPY ./main.js //Unit_Budget/main.js

COPY ./nodemon.json /src/nodemon.json

ENV NODE_ENV development

RUN npm start 
