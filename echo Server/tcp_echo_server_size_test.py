import socket

HOST = '0.0.0.0'
PORT = 5690

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

                recv_buffer = bytearray()
                current_chunk_size = 10

                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        print("Verbindung geschlossen.")
                        break

                    recv_buffer += data
                    print(f"Empfangen: {data} (Puffer: {len(recv_buffer)} Bytes)")

                    while len(recv_buffer) >= current_chunk_size:
                        chunk = recv_buffer[:current_chunk_size]
                        del recv_buffer[:current_chunk_size]

                        client_socket.sendall(chunk)
                        print(f"→ Gesendet {current_chunk_size} Bytes: {chunk}")

                        current_chunk_size += 10
                        if current_chunk_size > 150:
                            current_chunk_size = 10  # Wieder von vorne

if __name__ == "__main__":
    start_echo_server()
