import socket

HOST = '0.0.0.0'  # Server-Adresse (0.0.0.0 = alle Interfaces)
PORT = 5000      # Beliebiger freier Port

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
                    print(f"Empfangen: {data.decode().strip()}")
                    client_socket.sendall(data)

if __name__ == "__main__":
    start_echo_server()

# sudo lsof -i :5000
# sudo kill xxx
