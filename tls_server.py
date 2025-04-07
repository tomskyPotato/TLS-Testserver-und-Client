import socket
from tlslite import TLSConnection, X509, X509CertChain, parsePEMKey
from tlslite.handshakesettings import HandshakeSettings
from tlslite.messages import ClientHello, ServerHello, ServerKeyExchange, Certificate
from tlslite.utils.codec import Writer, Parser
from tlslite.constants import HandshakeType, ExtensionType

# Debug mode
import logging
logging.basicConfig(level=logging.DEBUG)

# Um die Session über das Terminal zu killen: sudo lsof -i :5000
HOST = "0.0.0.0"
PORT = 5000

def create_server_hello():
    # Create a ServerHello message
    server_hello = ServerHello()
    server_hello.create(
        version=(3, 3),
        random=getRandomBytes(32),
        session_id=getRandomBytes(32),
        cipher_suite=0x0035,  # Example cipher suite
        certificate_type=None,
        tackExt=None,
        next_protos_advertised=None,
        extensions=None
    )
    return server_hello

cert_path = "serverCert.pem"
key_path = "serverKey.pem"

x509 = X509().parse(open(cert_path).read())
cert_chain = X509CertChain([x509])
private_key = parsePEMKey(open(key_path).read(), private=True)

# Server-Socket einrichten
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[TLS] Server läuft auf {HOST}:{PORT} und wartet auf TLS-Client...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"[+] Verbindung von {addr}")

    tls_conn = TLSConnection(client_socket)

    try:
        tls_conn.handshakeServer(certChain=cert_chain, privateKey=private_key)
        print("[✓] Handshake abgeschlossen")

        data = tls_conn.read()
        print("[Daten empfangen]", data)

        tls_conn.write(b"Echo vom TLS-Server")
        tls_conn.close()

    except Exception as e:
        print("[!] TLS Fehler:", e)
