import socket

def connect_to_server(ip, port):
    try:
        # Cria um socket TCP/IP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Conecta ao servidor
            s.connect((ip, port))
            print(f"Conectado ao servidor {ip} na porta {port}")
    except Exception as e:
        print(f"Erro ao conectar ao servidor: {e}")

if __name__ == "__main__":
    server_ip = "52.91.66.12"
    server_port = 80
    connect_to_server(server_ip, server_port)
