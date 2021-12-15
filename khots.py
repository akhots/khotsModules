#!/usr/bin/env python3


# Convert IP to RAW

def ipRaw(ip):
    ip = ip.split('.')
    raw = int(ip[0])*256**3 + int(ip[1])*256**2 + \
        int(ip[2])*256**1 + int(ip[3]*256**0)
    return raw


# Convert RAW to IP

def rawIp(raw):
    a = raw // 256**3
    raw = raw - a*256**3
    b = raw // 256**2
    raw = raw - b*256**2
    c = raw // 256**1
    raw = raw - c*256**1
    d = raw // 256**0
    return f'{a}.{b}.{c}.{d}'


# Convert prefix to mask and wildcard mask
# import rawIp

def pref2mask(pref):
    return rawIp(4294967296 - 2**(32-pref))

def pref2wmask(pref):
    return rawIp(2**(32-pref) - 1)


# Resolve Name to IP addresses

def resolve(name, server=''):
    from os import popen
    from re import findall
    raw = popen('nslookup ' + name + ' ' + server).read()
    raw = ' '.join(raw.split('\n')[2:])
    return findall('\d+\.\d+\.\d+\.\d+',raw)

