#!/bin/bash
. lancache_config.sh
docker rm -f lancache
sudo mount $LANCACHE_RAID /cache/data
docker run -e CACHE_DISK_SIZE=2000g $LANCACHE_PARAMS