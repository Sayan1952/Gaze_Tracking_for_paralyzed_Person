

import cv2
from gaze_tracking import GazeTracking
import socket
import time

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)


# Creating a socket
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # Replace with the IP address or hostname of the receiving machine
port = 12345  # Choose a suitable port number


# Connecting to the receiver
sender_socket.connect((host, port))




while True:

    # We get a new frame from the webcam
    _, frame = webcam.read()

        # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    sender_socket.send(text.encode())



    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)


    if cv2.waitKey(1) == 27:
        break

webcam.release()
cv2.destroyAllWindows()






# if __name__ == "__main__":
#     queue = multiprocessing.Queue()
#     producer_process = multiprocessing.Process(target=producer, args=(queue,))
#     producer_process.start()
#
#     while True:
#         # Continuously check for data from the producer
#         data = queue.get()
#         print("Script 2 received:", data)




