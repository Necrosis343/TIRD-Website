# Python HTTP server

print("\nInitiating socket...\n")
import socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("\nSocket initiated!\n")
except socket.error as err:
	print(f"\nSocket failure!\n{err}\n")

print("\nBinding socket...\n")
ip="192.168.0.165"
port=80
wait=True
t=10
while wait:
	try:
		s.bind((ip,port))
		print(f"\nSocket binded to {ip}:{port}\n")
		wait=False
	except socket.error as err:
		print(f"\nBinding failure!\n{err}\n")
		import time
		print(f"\nWaiting {t} seconds\n")
		time.sleep(10)
s.listen(5)
print("\nSocket is listening...\n")
while True:
	try:
		c,addr=s.accept()
		print(f"{addr} has connected.")
		print(c.recv(1000).decode())
		c.send('HTTP/1.0 200 OK\n'.encode())
		print(c.recv(1000).decode())
		c.send('Content-Type: text/html\n'.encode())
		print(c.recv(1000).decode())
		c.send('\n'.encode())
		c.send("""<!DOCTYPE html><html><head><title>TIRD</title></head><body><h1>Hello</h1></body></html>""".encode())
		print(c.recv(1000).decode())
		c.close()
	except socket.error as err:
		print(f"\nCommunication error!\n{err}\n")
