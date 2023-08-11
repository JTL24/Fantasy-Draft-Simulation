### API ###
FROM python:3.10-slim

# Suppress warnings about running pip as root
ENV PIP_ROOT_USER_ACTION=ignore

RUN pip3 install pip --upgrade
RUN pip3 install setuptools --upgrade

COPY client_api/test/requirements.txt test-requirements.txt
RUN pip3 install -r test-requirements.txt

COPY client_api/api/requirements.txt api-requirements.txt
RUN pip3 install -r /api-requirements.txt

# Main API
COPY client_api /app
VOLUME /app
WORKDIR /app

COPY --chmod=0755 .docker/client_api/entrypoint.sh /usr/local/bin/entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["entrypoint.sh"]