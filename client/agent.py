import socket
import time
import json

class ClientAgent:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def register(self):
        self.client_socket.connect((self.server_ip, self.server_port))
        self.client_socket.sendall(json.dumps({'action': 'register'}).encode())
        response = self.client_socket.recv(1024)
        print('Registration response:', response.decode())

    def send_heartbeat(self):
        while True:
            self.client_socket.sendall(json.dumps({'action': 'heartbeat'}).encode())
            print('Heartbeat sent')
            time.sleep(10)

    def execute_command(self, command):
        self.client_socket.sendall(json.dumps({'action': 'execute', 'command': command}).encode())
        response = self.client_socket.recv(1024)
        print('Command response:', response.decode())

    def close_connection(self):
        self.client_socket.close()

if __name__ == '__main__':
    agent = ClientAgent('127.0.0.1', 5000)  # Update with server IP and port
    agent.register()
    # Optionally, start heartbeats in a separate thread
    # agent.send_heartbeat() # Uncomment to enable heartbeat functionality
    # agent.execute_command('ls')  # Example command
