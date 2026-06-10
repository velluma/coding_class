import socket

# IP_ADDR = "127.0.0.1" # 같은 컴퓨터에서 접속해올 때
# IP_ADDR = "192.168.1.10"
# socket.gethostname() : 내 컴퓨터 이름을 반환
# socket.gethostbyname() : 그 이름을 IP로 변환
# print(socket.gethostname())
# print(socket.gethostbyname("DESKTOP-04O81HS"))
IP_ADDR = socket.gethostbyname(socket.gethostname())

# https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
# PORT = 0  # 운영체제가 비어있는 포트에 배정
PORT = 7470

# AF_INET: IPv4
# AF_INET6: IPv6
# SOCK_STREAM: TCP (Transmission Control Protocol)
# SOCK_DGRAM: UDP (User Datagram Protocol)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 TCP 방식으로 통신할 준비

s.bind((IP_ADDR, PORT))  # 소켓에 IP 주소 연결
s.listen()  # 다른 컴퓨터로부터 연결을 받을 수 있도록 설정. 

print(f"Started server at {s.getsockname()}")

conn, addr = s.accept()  # 연결을 받아들임 (Blocking). 여기서 멈추고 기다림
# conn 에는 접속한 클라이언트 전용 소켓을 만들어 줌
# addr 에는 클라이언트의 (IP, 포트) 튜플. 예: ('192.168.0.5', 54321)

print(f"Connection from {addr}")

data = conn.recv(1024)  # 소켓을 통해서 최대 1024 바이트까지 데이터를 받아들임. 대기
# print(type(data))  # <class 'bytes'>

print("받은 데이터: ", data.decode("utf-8"))

conn.sendall(data)  # 받은 데이터를 그대로 돌려보냄

conn.close() # 클라이언트와의 연결 종료
s.close() # 서버 소켓 자체를 닫음 (더 이상 새 연결 안 받음)

print(f"Close connection from {addr}")
