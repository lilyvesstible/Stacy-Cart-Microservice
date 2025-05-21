import time
import zmq
from Cart_Functions import DecodeMessage

print("Starting Server. Looking for requests.")
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

cartList = []

#Operations: 
#0: Add Item
#1: Remove Item
#2: Clear List
#3: Print List
#4: Quit Server

while True:
    message = socket.recv()
    print(f"Received request from the client: {message.decode()}")
    if len(message) > 0:
        #result is a tuple, (Updated List, String To Print)
        result = DecodeMessage(message.decode(), cartList)
        cartList = result[0]
        time.sleep(1)
        socket.send_string(result[1])
        if result[1] == "[QUIT]":
            break

context.destroy()