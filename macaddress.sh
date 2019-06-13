#!/usr/bin/bash
API_KEY=$1
MAC_ADDRESS=$2
#Build the Image using  Dockerfile
docker image  build -t mac_addr .
#Run the container and pass API_KEY and MAC_ADDRESS as arguments
docker container run  mac_addr $API_KEY $MAC_ADDRESS
