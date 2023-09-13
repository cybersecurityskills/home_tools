import socket
import signal
import sys

def handler(signumb, frame):
   sys.exit()

signal.signal(signal.SIGINT, handler)

if len(sys.argv) < 3:
   print("Usage: socket_listener.py 192.168.200.4 8023") 
   sys.exit()


HOST = sys.argv[1]  # IP address to bind to 
PORT = int(sys.argv[2])  # Port to listen on (Ports < 1023 require root privileges) 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   s.bind((HOST, PORT))
   s.listen()
   while(1):
      conn, addr = s.accept()
      with conn:
         print(f"Connected by {addr}")
         while True:
            conn.sendall(b"This is a banner\n") 
            break
