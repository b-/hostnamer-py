# test.py
from namer import namer
from ipaddress import ip_interface as ipaddr
list_of_hosts = namer.HostList(firstip=ipaddr("192.168.12.34"),count=2)
for index, host in enumerate(list_of_hosts.hosts):
    print(f"name: {host.name}, ip: {host.ip}")
# foo-bar
# "192.168.12.34/32"
# baz-bat
# "192.168.12.35/32"
