#!/bin/bash
. lancache_config.sh
docker rm -f lancache
sudo umount /cache/data
docker run -e CACHE_DISK_SIZE=500g $LANCACHE_PARAMS