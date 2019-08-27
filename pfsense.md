# pfSense
pfSense is FreeBSD-based (thus the pf-prefix, from pf (equivalent to iptables)) operating system for routing IP-networks. pfSense gives you a web-UI (for when you want to make most changes) and a terminal interface (for when you want to touch the unix-innards, or when you've really 💢-ed it up).

## Packages used
To install packages, go to System -> Package Manager -> Available Packages.
### ntopng - Network TOP Next Generation

ntopng enables you to collect stats on network traffic. Which countries have the most traffic? What about IPs? Which apps are they using? Operating systems? Apps? Then you can filter on those, look up a map, etc.

ntopng is available through Diagnostics -> ntopng when installed. Must be enabled using Diagnostics -> ntopng Settings. To get country-stats, you also need to download the GeoIP database. ![](/images/pfSense-ntopng-conf-basic.png) In addition, you have to enable the various features for which you want to collect stats.<br/>
**Note:** ntopng does not use the authentication-system integrated in pfSense.<br/>
**Note:** To enable usage of the maps-functionality, you have to get a Google Maps API-key.

### Suricata Intrusion Detection/Prevention System

Suricata identifies threats and potential issues on **interfaces** according to **rules**. Rules are pulled from rulesets, which you can subscribe to. <br/>
**Note:** Since we're using multi-wan, rulesets have to be enabled and ignored separately on WAN1 and WAN2

### telegraf
![](/images/pfsense-howto-enable-influxdb-client.png)