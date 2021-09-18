import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1027        # The port used by the server
BUFFER_SIZE = 256

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    message = b'hello ATU'
    message_length = len(message)
    s.connect((HOST, PORT))
    s.sendall(message)
    
    amount_received = 0
    print('Received:')

    while amount_received < message_length:
        data = s.recv(BUFFER_SIZE)
        amount_received += len(data)
        print( repr(data) )
    

