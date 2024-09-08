from scapy.all import ARP, Ether, srp

def scan(interface, ip):
    arp_request = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp_request
    result = srp(packet, iface=interface, timeout=3, verbose=0)[0]
    
    # Parsing the result
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    return clients

if __name__ == "__main__":
    target_ip = "192.168.1.0/24"  # Replace with your network range
    interface = "wlan0"  # Replace with your interface
    clients = scan(interface, target_ip)

    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for client in clients:
        print(f"{client['ip']}\t\t{client['mac']}")

