FROM node:16
RUN mkdir /Unit_Budget

RUN apt-get update
RUN apt-get install -y --no-install-recommends python  python3-pip
RUN apt-get install -y python3-setuptools
RUN apt-get install -y python3-dev
    
WORKDIR /Unit_Budget

COPY ./package.json /Unit_Budget/package.json
COPY ./package-lock.json /Unit_Budget/package-lock.json

RUN npm install

## import the source code into the docker Unit budget
COPY ./src /Unit_Budget/src

COPY ./dist /Unit_Budget/dist

COPY ./Python_File /Unit_Budget/Python_File

RUN pip3 install -r /Unit_Budget/Python_File/requirements.txt

COPY ./preload.js /Unit_Budget/preload.js
COPY ./main.js //Unit_Budget/main.js

ENV NODE_ENV development

RUN npm start 
