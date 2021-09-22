import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 1027
BUFFER_SIZE = 512
HOST = '127.0.0.1'
PORT = 51630
HOST = '127.0.0.1'
PORT = 51633
HOST = '127.0.0.1'
PORT = 51634

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(4)

    conn, addr = s.accept()
    from_client = ''
    while True:
        data = conn.recv(1027)
        if not data: break
        from_client += data
        print from_client
        conn.send("I am SERVER<br>")
    conn.close()
    print 'client disconnected'
    with conn:
        print('Connection opened:', addr)

        # you may wish to use full_message
        # remember that it is a bytes array and if you
        # compare it to a string, you should convert
        # the string to a bytearray:  b'mystring'
        full_message = bytearray()
        while True:
            data = conn.recv(BUFFER_SIZE)
            full_message += data
            if not data: # if no data, break from loop
                break
            conn.sendall(data)
    
    print("Connection closed.")
