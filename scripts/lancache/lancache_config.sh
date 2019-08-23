export LAN_IP="172.16.0.50" # Actual CampusLAN

export LANCACHE_RAID="/dev/md0" # output from mdadm --detail --scan
export LANCACHE_PARAMS="-e UPSTREAM_DNS=8.8.8.8 -e CACHE_MEM_SIZE=24000m -e NGINX_WORKER_PROCESSES=100 --restart unless-stopped --log-opt max-size=10m --log-opt max-file=3 --name lancache --detach -v /cache/data:/data/cache -v /cache/logs/:/data/logs -p 80:80 lancachenet/monolithic:latest"