#Retrieve 3.9 python version
FROM python:3.9

#Create code directory in docker container
WORKDIR /usr/app

#Required for the analyzer's metrics endpoint to be accessible by Prometheus
ENV PROMETHEUS_MULTIPROC_DIR=/tmp

#Copy all project files and directories in docker container
COPY * ./
COPY ./routes ./routes
COPY ./services ./services

#Download poetry package manager
RUN pip install poetry

#Install project dependencies
RUN poetry install

#Replace prediction endpoint host by its container name
RUN sed -i "s/PREDICTION_MODEL_HOST=[']127[.]0[.]0[.]1[']/PREDICTION_MODEL_HOST='toxicity_analyzer_model'/g" /usr/app/.env

#Define application and Prometheus server running ports
EXPOSE 5000 8010

#Lauch app after container be instantiated
CMD ["poetry", "run", "flask", "run"]