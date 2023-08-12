# Fantasy Draft Simulation

This is the backend for a Fantasy Draft Simulation. 

It is able to locally deploy and test using Docker and Fly. 

Uses FASTAPI with python to find and create players from a database. 

# Instructions 

Create a local.env file in your .docker folder, with your api key (wrapped in quotes), like:
FLY_API_TOKEN="[your api token value]"

docker-compose build

docker-compose up

From a new terminal window, run:
docker ps
  (It should include something like "football_tools_1")

Open a shell in the tools container:
docker exec -it football_tools_1 /bin/bash

Run Flyctl launch to create a new application:
cd /app
flyctl launch --path .docker/client_api/ --dockerfile Dockerfile

This will create a config file at: .docker/client_api/fly.toml

10. Deploy your API from the config file:
flyctl deploy -c .docker/client_api/fly.toml

It's mapped to localhost:80, so it will open in a web browser
