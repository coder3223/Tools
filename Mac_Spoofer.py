import subprocess
import optparse
import re
# original MAC Address 08:00:27:af:ab:05


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Specify interface to change MAC Address")
    parser.add_option("-m", "--mac-address", dest="new_mac_addr", help="Specify the MAC Address you want to use")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, user --help for more info.")
    if not options.new_mac_addr:
        parser.error("[-] Please specify an MAC Address, user --help for more info.")
    return options


def change_mac(interface, new_mac_addr):
    print(f"[+] Changing the MAC Address for {interface} to new MAC Address {new_mac_addr}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_addr])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    if_config_result = subprocess.check_output(["ifconfig", interface])
    mac_addr_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(if_config_result))
    if mac_addr_search_result:
        return mac_addr_search_result.group(0)
    else:
        print("Could NOT read MAC Address.")


parameters = get_argument()
current_mac = get_current_mac(parameters.interface)
print(f"[+] Current MAC: {str(current_mac)}")
change_mac(parameters.interface, parameters.new_mac_addr)
current_mac = get_current_mac(parameters.interface)

if current_mac == parameters.new_mac_addr:
    print(f"[+] MAC Address successfully changed to {parameters.new_mac_addr}")
else:
    print("[-] MAC Address could not be changed.")
