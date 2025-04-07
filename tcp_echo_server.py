import socket
import tlslite
print(tlslite.__file__)
server_hello_header = b'\x02\x00\x00\x4d\x03'

HOST = '0.0.0.0'  # Server-Adresse (0.0.0.0 = alle Interfaces)
PORT = 5690       # Beliebiger freier Port

def start_echo_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Echo-Server läuft auf {HOST}:{PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Verbindung von {client_address}")
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break  # Verbindung beendet
                    #nachricht = data.decode().strip()
                    print(f"Empfangen: {data}")
                    client_socket.sendall(server_hello_header + server_hello_header)
                    print(f"Echo zurückgesendet: {repr(server_hello_header)}")

if __name__ == "__main__":
    start_echo_server()

# sudo lsof -i :5690
# sudo kill xxx
