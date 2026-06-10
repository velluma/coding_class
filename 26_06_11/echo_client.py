import socket

SERVER_IP = "192.168.0.7"  # 접속할 서버의 IP 주소를 명확히 지정
SERVER_PORT = 7470  # # 접속할 서버의 포트를 명확히 지정

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 서버와 동일하게 IPv4 TCP 소켓 생성

s.connect((SERVER_IP, SERVER_PORT))  # 서버에 연결 (Blocking)

s.sendall("Hello, Internet!".encode("utf-8"))  # 소켓을 통해서 데이터 보내기

data = s.recv(1024)  # 소켓을 통해서 최대 1024 바이트까지 데이터를 받아들임

print("돌려받은 데이터: ", data.decode("utf-8"))
