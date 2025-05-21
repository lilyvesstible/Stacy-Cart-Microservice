import time
import zmq
from Cart_Functions import DecodeMessage

print("Starting Server. Looking for requests.")
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

cartList = []

while True:
    message = socket.recv()
    print(f"Received request from the client: {message.decode()}")
    if len(message) > 0:
        #result is a tuple, (Updated List, String To Print)
        result = DecodeMessage(message.decode(), cartList)
        if result[1] == "[QUIT]":
            break
        cartList = result[0]
        time.sleep(3)
        socket.send_string(result[1])

context.destroy()