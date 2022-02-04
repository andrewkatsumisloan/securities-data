FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip

WORKDIR /backend-securities

EXPOSE 5000
ENV PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV PYTHONPATH = "/backend-securities"

# RUN mkdir -p /var/tmp/tag_session
# COPY setup.py .

# COPY ./core ./core
# COPY ./data_scripts ./data_scripts
# COPY ./model ./model
# COPY ./model_run ./model_run


RUN pip install pipenv
COPY Pipfile .
RUN ls Pipfile
RUN pipenv lock --requirements > requirements.txt && \
    pip install -r requirements.txt



