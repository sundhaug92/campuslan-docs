# Concerto

Concerto is a centralised digital-signage solution, powering the kiosk menu-screens and main screen. This was first implemented with 2019V.
Hosted on port 80 on [VM X](vms/X.md).

## Concerto basics
In Concerto, **content** is published to **feeds**. A feed is subscribed to by a **field** of a **template** on a **screen**. Screens are owned either by **users** or **user-groups**. **Feeds** can have **sub-feeds**, from which they pull their content, which are owned by a different user or group. Content in feeds can have a set start and end time (NB! This is according to the time of the screen, not the server, and when scheduled the times are known to anyone).

## Installation
### Requirements
- Ubuntu 16.04 LTS or Debian 9 (stretch)

### HOWTO
```
curl http://get.concerto-signage.org/add_repo.sh | sh
```

If using Ubuntu 16.04, modify `/etc/apt/sources.d/concerto.list` so the passenger repo references `xenial` rather than `stretch`, `sudo apt update` (to update cache), unless [concerto/concerto-debian#71](https://github.com/concerto/concerto-debian/pull/72) is merged.
`sudo apt install concerto-full`. If the VM is not available with the domain-name `concerto`, then `/etc/apache2/sites-enabled/concerto.conf` should be modified so either ServerName matches or is commented out. If you comment out ServerName, run `sudo a2dissite 000-default.conf` to disable the default site. After this, run `service apache2 reload`. Open your browser and go to the IP of the host (or localhost) to register the first user. Go to /settings, then click permissions, disable "Allow open user registration", and click save.