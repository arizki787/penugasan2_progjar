import socket

def send_request(request):
    host = 'localhost'
    port = 45000
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(request.encode('utf-8'))
        response = s.recv(1024)
        print(f"Response: {repr(response.decode('utf-8'))}")

if __name__ == "__main__":
    # Contoh penggunaan
    send_request("TIME\r\n")
    send_request("QUIT\r\n")