import socket
from urllib.parse import parse_qs
import pymongo
import datetime
import logging

logging.basicConfig(level=logging.INFO)

client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.rqsgk8e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["chat"]
collection = db["chat"]

def handle_data(data):
    print("Received data:", data)
    parsed_data = parse_qs(data.decode())
    collection.insert_one({
        "username": parsed_data["username"][0],
        "message": parsed_data["message"][0],
        "date": datetime.datetime.now()
    })

SERVER_ADDRESS = ('', 5000)
print("Socket server is starting...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen(1)
    print("Socket server is listening on port 5000")

    while True:
        client_socket, client_address = server_socket.accept()
        print("Client connected:", client_address)

        data = client_socket.recv(1024)
        if data:
            handle_data(data)

        client_socket.close()
