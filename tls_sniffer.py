from scapy.all import sniff, TCP, Raw

def packet_callback(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        payload = pkt[Raw].load
        if b'\x16\x03\x01' in payload or b'\x16\x03\x03' in payload:  # TLS Handshake
            print(f"[TLS] {pkt[IP].src}:{pkt[TCP].sport} -> {pkt[IP].dst}:{pkt[TCP].dport}")
            print(payload.hex())

print("[*] Starte TLS-Sniffer auf Port 5000...")
sniff(filter="tcp port 5000", prn=packet_callback, store=0)
