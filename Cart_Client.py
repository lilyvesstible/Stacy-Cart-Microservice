#For debugging purposes. Should not be used for product
import zmq

print("Client attempting to connect to server...")
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
    print("Type a Command")
    command = input()
    if command == "q":
        break
    socket.send_string(command)
    message = socket.recv()
    print(message.decode())