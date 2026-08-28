from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw


def process_packet(packet):
    print("\n" + "=" * 60)
    print("[+] PACKET CAPTURED")
    print("=" * 60)

    # Check whether the packet contains an IP layer
    if IP in packet:

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        print(f"Source IP        : {source_ip}")
        print(f"Destination IP   : {destination_ip}")

        # Identify TCP packets
        if TCP in packet:
            print("Protocol         : TCP")
            print(f"Source Port      : {packet[TCP].sport}")
            print(f"Destination Port : {packet[TCP].dport}")

        # Identify UDP packets
        elif UDP in packet:
            print("Protocol         : UDP")
            print(f"Source Port      : {packet[UDP].sport}")
            print(f"Destination Port : {packet[UDP].dport}")

        # Identify ICMP packets
        elif ICMP in packet:
            print("Protocol         : ICMP")

        else:
            print("Protocol         : Other")

        # Display payload when available
        if Raw in packet:
            payload = bytes(packet[Raw].load)

            print(f"Payload Length   : {len(payload)} bytes")

            # Display a small portion of the payload
            print(f"Payload Preview  : {payload[:50]!r}")

        else:
            print("Payload          : None")

    else:
        print("Non-IP packet")


print("=" * 60)
print("       CODEALPHA BASIC NETWORK SNIFFER")
print("=" * 60)
print("[*] Starting packet capture...")
print("[*] Press CTRL+C to stop.")
print("=" * 60)

# Start capturing packets
sniff(prn=process_packet, store=False)