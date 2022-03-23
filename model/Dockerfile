#Retrieve 3.9 python version
FROM python:3.9

#Create code directory in docker container
WORKDIR /usr/app

#Required for the model's metrics endpoint to be accessible by Prometheus
ENV PROMETHEUS_MULTIPROC_DIR=/tmp

#Copy all project files and directories in docker container
COPY * ./
COPY ./routes ./routes 
COPY ./services ./services 

#Download poetry package manager
RUN pip install poetry

#Install project dependencies
RUN poetry install

#Define application and Prometheus server running ports
EXPOSE 8000 8010

#Lauch app after container be instantiated
CMD ["poetry", "run", "flask", "run"]