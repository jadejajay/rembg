import socket
import time
import random

def produce_messages():
    while True:
        message = f"Message: {random.randint(1, 100)}"
        yield message
        time.sleep(random.uniform(0.1, 1))

if __name__ == "__main__":
    server_address = ("localhost", 12345)  # Change as needed

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(server_address)
        server_socket.listen(1)

        print("Producer: Waiting for a connection...")
        connection, client_address = server_socket.accept()

        try:
            with connection:
                print(f"Producer: Connection established with {client_address}")
                for message in produce_messages():
                    connection.sendall(message.encode())
                    print(f"Produced: {message}")
        except Exception as e:
            print(f"Producer: Error - {str(e)}")
