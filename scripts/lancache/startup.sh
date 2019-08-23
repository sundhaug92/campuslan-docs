#!/bin/bash
set -e
set -u
. lancache_config.sh # Load config

if docker ps -a | grep "lancache-dns" > /dev/null
then
    docker rm -f lancache-dns > /dev/null
fi
if docker ps -a | grep "sniproxy" > /dev/null
then
    docker rm -f sniproxy > /dev/null
fi

docker run -d --name sniproxy -p 443:443/tcp lancachenet/sniproxy
docker run -d --name lancache-dns -p $LAN_IP:53:53/udp -e USE_GENERIC_CACHE=true -e LANCACHE_IP=$LAN_IP lancachenet/lancache-dns
./disable-yolo-mode.sh