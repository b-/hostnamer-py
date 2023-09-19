# namer.py
from ipaddress import ip_interface as ipif
from xkcdpass import xkcd_password as xp

def generate_hostname(numwords=2, minlength=2, count=1):
    wordfile = xp.locate_wordfile()
    wordlist = xp.generate_wordlist(wordfile=wordfile,min_length=minlength)
    hostnames = []
    for hostname in range(0, count):
        hostnames.append(xp.generate_xkcdpassword(wordlist=wordlist,numwords=numwords,delimiter="-"))
    return hostnames

class IpHost:
    """an instance"""
    def __init__(self, ip, name=generate_hostname()) -> any:
        self.name = name
        self.ip = ipif(ip)

class HostList:
    def __init__(self, count, firstip = ipif("192.168.12.34/24")):
        self.hosts = []
        for i in range(count):
            _=IpHost(ip=(firstip + (i)), name=generate_hostname())
            self._add_host(ip=_.ip, name=_.name)

    def _add_host(self, ip, name):
        self.hosts.append(IpHost(ip=ip, name=name))
