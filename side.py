import tkinter as tk
import time
from tkinter import messagebox



import mouse
import socket

# Creating a socket
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

def select_button(condition):
    if condition == "Looking left":
        left_button.focus_set()
    elif condition == "Looking right":
        right_button.focus_set()
    elif condition == "Looking center":
        center_button.focus_set()


# while True:
#     # Receive data from the sender
#     data = connection.recv(1024).decode()
#
#     if not data:
#         break
#
#     print("Script 2 received:", data)  # Process or display the received data
#
def button_clicked(text):
    mouse.click('left')
    label.config(text='button pressed')


# Close the connection and socket when done
# connection.close()
# receiver_socket.close()

# Function to handle button clicks for left option
def left_option_clicked():
    label.config(text="Left option clicked")

# Function to handle button clicks for right option
def right_option_clicked():
    label.config(text="Right option clicked")

# Function to handle button clicks for top option
def top_option_clicked():
    label.config(text="Top option clicked")

# Function to handle button clicks for bottom option
def bottom_option_clicked():
    label.config(text="Bottom option clicked")

# Function to select a button based on external condition




# if __name__ == "__main__":
#     queue = multiprocessing.Queue()
#     consumer_process = multiprocessing.Process(target=consumer, args=(queue,))
#     consumer_process.start()
#
#     while True:
#         # Simulate generating live data (replace this with your actual data source)
#         data = "Live data from script 2 at " + str(time.time())
#         queue.get(data)
#         time.sleep(1)  # Adjust the sleep time as needed

root = tk.Tk()
root.title("Gaze Controlled Options")

# Set the fixed size of the window (width x height)
window_width = 1300
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Create buttons for left, right, top, and bottom options
left_button = tk.Button(root, text="Yes", command=button_clicked)
right_button = tk.Button(root, text="Help", command=button_clicked)
center_button = tk.Button(root, text="No", command=button_clicked)


# Create a label to display selected option
label = tk.Label(root, text="Press a button to select an option")



# Place buttons and label on the left side
label.pack(side="top")
left_button.pack(side="left", padx=60, pady=40)
right_button.pack(side="right", padx=60, pady=40)
center_button.pack(side="top", padx=60, pady=40)





# Example: Simulate selecting a button based on an external condition
# Replace "external_condition" with your actual condition
# external_condition = "right"
# select_button(external_condition)
# Variables to track button focus and time
focused_button = None
focus_start_time = None


def checkData():
    global data, focused_button, focus_start_time
    # while True:
        # Receive data from the sender
    data = connection.recv(1024).decode()



    print("Script 2 received:", data)  # Process or display the received data
    if data == "blinking":
        if focused_button:
            # Simulate a left mouse button click to open a confirmation window
            open_confirmation_window()
            # Reset focus-related variables
            focused_button = None
    else:
        # Reset focus-related variables for other conditions
        focused_button = None

    select_button(data)

    root.after(100, checkData)





checkData()

root.mainloop()
