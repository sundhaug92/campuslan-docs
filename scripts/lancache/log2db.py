#!/usr/bin/env python3
# Takes the log from lancache and puts the details in a SQLite database, making it easier to parse
import re
import sqlite3
import sys


conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS access (cache_identifier TEXT, remote_address TEXT, http_x_forwarded_for TEXT, remote_user TEXT, time_local TEXT, method TEXT, path TEXT, status_code TEXT, body_bytes_sent TEXT, http_referer TEXT, http_user_agent TEXT, upstream_cache_status TEXT, host TEXT, http_range TEXT)')
conn.commit()


def handle_line(line):
    if line.startswith('[]'):
        return
    if line == '':
        return
    # print(line)
    # The following, monstrous, regex, extracts from a logline everything interesting
    m = re.search(r'^(\[[a-z0-9.]+\]) (([0-9]+\.){3}[0-9]+) \/ (-|[0-9.]+) (-) - \[([0-9]+\/[A-Za-z]+\/[0-9]+:([0-9]{2}:?){3} \+[0-9]+)\] "([A-Z]+) ([\/a-zA-Z0-9.\-_\?\=\&\%\~\+\:]+) HTTP\/[012]\.[01]" ([0-9]{3}) ([0-9]+) ("-") "([A-Za-z\/.0-9() \-\ .;,:_\+]+)" "([A-Z\-]+)" "([a-z0-9.\-]+)" "((-)|(bytes=[0-9\-]+))"$', line)
    # When this breaks, its' probably UA or path. Cut here                                                                                ^path or                                                                                  ^here (UA)
    if m is None:
        raise Exception('UNKNOWN LINE "{}"'.format(line))
    # cache_identifier: Which cache is this? ex: wsus (Windows Update), steam
    cache_identifier = m.group(1)
    if cache_identifier.startswith('[') and cache_identifier.endswith(']'):
        cache_identifier = cache_identifier[1:-1]
  #  print('cache_identifier', cache_identifier)
    # remote_address: Which IP requested this?
    remote_address = m.group(2)
  #  print('remote_address', remote_address)
    http_x_forwarded_for = m.group(4)
  #  print('http_x_forwarded_for', http_x_forwarded_for)
    remote_user = m.group(5)
  #  print('remote_user', remote_user)
    time_local = m.group(6)
    # time_local: What time is it? I don't know Zac Efron. Seriously though, this is the local time, with timezone specified
  #  print('time_local', time_local)
    method = m.group(8)
    # method: Sometimes you have to POST, to GET a HEAD, though you may have OPTIONS. Seriously though, this is the HTTP method.
  #  print('method', method)
    path = m.group(9)
    # path: This is the HTTP path
  #  print('path', path)
    status_code = m.group(10)
    # status_code: HTTP status code returned (did we find the resource requested for example). Ex: 200
  #  print('status_code', status_code)
    body_bytes_sent = m.group(11)
    # body_bytes_sent: How much did we return
  #  print('body_bytes_sent', body_bytes_sent)
    http_referer = m.group(12)
  #  print('http_referer', http_referer)
    http_user_agent = m.group(13)
    # http_user_agent: Tells you what sort of client made the request. Say "Valve/Steam HTTP Client 1.0" (Steam)
  #  print('http_user_agent', http_user_agent)
    upstream_cache_status = m.group(14)
    # upstream cache status. Like Star Trek movies, this is usually either a "HIT" (meaning we had this in the cache) or a "MISS" (meaning we didn't)
  #  print('upstream_cache_status', upstream_cache_status)
    host = m.group(15)
    # Domain-name requested. Sent by the client in HTTP/1.1+ so you can host multiple domains on one IP (which lancache tends to do)
  #  print('host', host)
    http_range = m.group(16)
  #  print('http_range', http_range)
#    for _ in range(3,20): print(_, m.group(_))
    c.execute('INSERT INTO access VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (cache_identifier, remote_address, http_x_forwarded_for, remote_user, time_local, method, path, status_code, body_bytes_sent, http_referer, http_user_agent, upstream_cache_status, host, http_range))
#    conn.commit()

fname = sys.argv[1] if len(sys.argv) > 1 else '/cache/logs/access.log'
for line in open(fname).read().split('\n'):
    handle_line(line)
#    break
conn.commit()
conn.close()