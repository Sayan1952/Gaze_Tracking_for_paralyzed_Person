import socket

# Create a socket
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # Replace with the IP address or hostname of the receiving machine
port = 12345  # Use the same port number as in Script 1

# Bind the socket to the host and port
receiver_socket.bind((host, port))

# Listen for incoming connections
receiver_socket.listen(1)

print("Waiting for a connection...")
connection, address = receiver_socket.accept()
print("Connected by", address)

while True:
    # Receive data from the sender
    data = connection.recv(1024).decode()

    if not data:
        break

    print("Script 2 received:", data)  # Process or display the received data

# Close the connection and socket when done
connection.close()
receiver_socket.close()
