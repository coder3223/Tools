#!/usr/bin/env python3


import scapy.all as scapy
import argparse


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP Range with CIDR")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please enter a network address to scan")
    return options


def scan(ip):
    answer_list = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ip), timeout=2, verbose=False)[0]
    client_list = []
    for item in answer_list:
        client_dict = {"IP": item[1].psrc, "MAC": item[1].hwsrc}
        client_list.append(client_dict)
    return client_list


def display(scan_result):
    print("IP\t\t\tMAC ADDRESS")
    print("-" * 41)
    for client in scan_result:
        print(f"{client['IP']}\t\t{client['MAC']}")


network = get_options()
results = scan(network.target)
display(results)
