import socket
import time

# Create a socket
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # Replace with the IP address or hostname of the receiving machine
port = 12345  # Choose a suitable port number

# Connect to the receiver
sender_socket.connect((host, port))

while True:
    # Simulate generating live data (replace this with your actual data source)
    data = "apple"

    # Send the data over the socket
    sender_socket.send(data.encode())

    time.sleep(1)  # Adjust the sleep time as needed

# Close the socket when done
sender_socket.close()
