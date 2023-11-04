import socket

def consume_messages():
    client_address = ("localhost", 12345)  # Change to match the producer's server_address

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(client_address)

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"Consumed: {message}")

if __name__ == "__main__":
    consume_messages()
