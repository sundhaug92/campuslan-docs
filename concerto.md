# Concerto

Concerto is a centralised digital-signage solution, powering the kiosk menu-screens and main screen. This was first implemented with 2019V.
Hosted on port 80 on [VM X](vms/X.md).

## Installation
### Requirements
- Ubuntu 16.04 LTS or Debian 9 (stretch)

## HOWTO
```
curl http://get.concerto-signage.org/add_repo.sh | sh
```

If using Ubuntu 16.04, modify `/etc/apt/sources.d/concerto.list` so the passenger repo references `xenial` rather than `stretch`, `sudo apt update` (to update cache), unless [concerto/concerto-debian#71](https://github.com/concerto/concerto-debian/pull/72) is merged.
`sudo apt install concerto-full`.