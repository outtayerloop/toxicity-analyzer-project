#Create NodeJS Image 
FROM node:16

#Define app folder in docker image
WORKDIR /usr/app

#Copy application content
COPY * ./   
COPY ./src ./src 
COPY ./monitoring ./monitoring

#Replace monitoring server endpoint host by its container name
RUN sed -i "s/[$][{]config[.]DEV_SERVER_HOST[}]/toxicity_analyzer_front/g" /usr/app/vue.config.js

#Install dependencies
RUN npm install

#Define the image port to listen
EXPOSE 3000

#Command to run for launching app
CMD ["npm", "run", "serve"]