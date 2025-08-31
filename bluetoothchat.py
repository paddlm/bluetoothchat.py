import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

print("Warte auf Verbindung...")
client_sock, client_info = server_sock.accept()
print(f"Verbunden mit {client_info}")

try:
    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        print("Client sagt:", data.decode())
        msg = input("Du: ")
        client_sock.send(msg.encode())
except OSError:
    pass

print("Verbindung beendet")
client_sock.close()
server_sock.close()


import bluetooth

server_mac = input("MAC-Adresse des Servers: ")  # z. B. '00:1A:7D:DA:71:13'
port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((server_mac, port))
print("Verbunden mit Server!")

try:
    while True:
        msg = input("Du: ")
        sock.send(msg.encode())
        data = sock.recv(1024)
        print("Server sagt:", data.decode())
except OSError:
    pass

print("Verbindung beendet")
sock.close()


