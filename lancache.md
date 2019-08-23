# LANCACHE
Lancache uses DNS-trickery, Nginx and sniproxy to cache static content from servers we expect to be used a lot.
Hosted on [lancache](./devices/lancache.md).
The lancache is configured to use the RAID0 SSDs for caching by default, but this can be disabled by running the disable-yolo-mode.sh script.

Every wednesday morning, if the machine is up, a cron-job pulls down the latest container-images. This can also be triggered by running a script.