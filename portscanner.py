#!/usr/bin/env python3

import socket
from IPy import IP


def scan(target):
    converted_ip = check_ip(target)
    print(f"\nScanning target: {str(target)}")
    for port in range(1, 100):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(s):
    return sock.recv(1024)


def scan_port(ipaddr, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ipaddr, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip("\n")))
        except:
            print(f"[+] Open Port {str(port)}")
    except:
        pass


targets = input("[+] Enter target(s) to scan(split targets with ',': ")

if ',' in targets:
    for ipaddr in targets.split(','):
        scan(ipaddr.strip(' '))
else:
    scan(targets)

