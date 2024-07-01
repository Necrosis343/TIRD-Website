# Python test socket

print("\nInitiating socket...\n")
import socket
try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("\nSocket initiated!\n")
except socket.error as err:
        print(f"\nSocket failure!\n{err}\n")

print("\nConnecting to server\n")
try:
	s.connect(("192.168.0.165",80))
except socket.error as err:
	print(f"\nConnection failure!\n{err}\n")
while True:
	s.send("lol".encode())
	print(s.recv(1000).decode())
	#s.close()
