import socket
from contextlib import closing

def scan_port(ip, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.settimeout(1)  # Define o tempo limite para conexão em 1 segundo
        result = sock.connect_ex((ip, port))
        if result == 0:
            service = input(f"A porta {port} está aberta. Digite o serviço associado: ")
            print(f"A porta {port} está aberta. Serviço: {service}")
        else:
            print(f"A porta {port} está fechada")

def main():
    ip = input("Digite o endereço IP para verificar as portas abertas: ")
    max_port = 65535  # Número máximo de porta a serem verificadas

    for port in range(1, max_port + 1):
        scan_port(ip, port)

if __name__ == "__main__":
    main()
