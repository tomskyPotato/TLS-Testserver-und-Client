import socket
from tlslite import TLSConnection
from tlslite import HandshakeSettings
from tlslite.extensions import SupportedGroupsExtension
from tlslite.constants import GroupName

HOST_HOME = "127.0.0.1"         # dns_utils.py wurde erweitert um localhost zuzulassen
HOST_THOMAS = "84.145.16.38"
HOST_WEPTECH = "weptech-iot.de"

PORT_THOMAS = 5000
PORT_WEPTECH = 5690
PORT_DEBUG = 5001

# Host und Port hier Ändern zur Nutzung im Programm
HOST = HOST_HOME
PORT = PORT_WEPTECH

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"[+] Verbunden mit {HOST}:{PORT}")

    tls_conn = TLSConnection(client_socket)

    settings = HandshakeSettings()
    settings.alpnProtocols = ["http/1.1"]

    tls_conn.handshakeClientCert(settings=settings, serverName=HOST)


    try:
        print("[*] Starte TLS-Handshake (anonym)...")
        tls_conn.handshakeClientAnonymous()
        print("[✓] TLS-Handshake erfolgreich")

        tls_conn.write(b"Hallo Server vom Client")
        response = tls_conn.read()
        print("[<] Antwort vom Server:", response.decode())

    except Exception as e:
        print("[!] TLS Fehler:", e)

    finally:
        tls_conn.close()
        client_socket.close()
        print("[x] Verbindung geschlossen")

if __name__ == "__main__":
    main()
