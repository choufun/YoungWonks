import socket

HOST = '0.0.0.0'
PORT = 1234

'''
try:
    data = s.recv(BUFFER_SIZE)
except socket.error:
    s.close()
finally:
    s.close()
'''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print('Received', data)
            conn.sendall(input('Enter: ').encode())
