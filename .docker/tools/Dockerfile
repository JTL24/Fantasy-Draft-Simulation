### Tools ###
FROM node:19.3-buster-slim

#FROM python:3.10-slim
#FROM docker:20-dind
#FROM flyio/flyctl

RUN apt-get update
RUN apt-get install -y curl

RUN curl -L https://fly.io/install.sh | sh

ENV FLYCTL_INSTALL="/root/.fly"
ENV PATH="${PATH}:${FLYCTL_INSTALL}/bin"

COPY . /app
VOLUME /app

COPY --chmod=0755 ./.docker/tools/entrypoint.sh /usr/local/bin/entrypoint.sh

WORKDIR /app

ENTRYPOINT ["entrypoint.sh"]