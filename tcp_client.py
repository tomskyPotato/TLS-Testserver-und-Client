import socket

HOST = '127.0.0.1'  # Adresse des Servers
PORT = 5000        # Muss mit dem Server-Port übereinstimmen

def start_echo_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Verbunden mit {HOST}:{PORT}")

        while True:
            message = input("Nachricht eingeben (oder 'exit' zum Beenden): ")
            if message.lower() == 'exit':
                print("Verbindung wird geschlossen.")
                break
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Antwort vom Server: {data.decode().strip()}")

if __name__ == "__main__":
    start_echo_client()
