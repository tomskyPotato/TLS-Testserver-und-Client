import socket
from tlslite import TLSConnection

HOST = "127.0.0.1"
PORT = 5000

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"[+] Verbunden mit {HOST}:{PORT}")

    tls_conn = TLSConnection(client_socket)

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
