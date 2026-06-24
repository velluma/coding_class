import socket

IP_ADDR = socket.gethostbyname(socket.gethostname())
PORT = 80

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.bind((IP_ADDR, PORT))
my_socket.listen(5)
print(f"Started server at {my_socket.getsockname()}")

while True:
    conn, addr = my_socket.accept()
    request = conn.recv(1024).decode()
    print(request)

    try:
        path = request.split(" ")[1]
    except IndexError:
        conn.close()
        continue

    if path == "/cat.jpg":
        with open("cat.jpg", "rb") as f:
            body = f.read()
        header = "HTTP/1.0 200 OK\r\nContent-Type: image/jpeg\r\n\r\n"
        conn.sendall(header.encode() + body)
    else:
        with open("index.html", "rb") as f:
            body = f.read()
        header = "HTTP/1.0 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
        conn.sendall(header.encode() + body)

    conn.close()

my_socket.close()