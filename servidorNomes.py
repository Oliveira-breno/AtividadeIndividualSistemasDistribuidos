
import socket
import json

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind(('127.0.0.1', 8008))
servidor.listen()

print('Servidor de nomeação aguardando conexões...')

servidores = {
    "+": ["127.0.0.1:8000", "127.0.0.1:8001"],
    "-": ["127.0.0.1:8000"],
    "/": ["127.0.0.1:8000"],
    "*": ["127.0.0.1:8000"],
    "**2": ["127.0.0.1:8000"],
    "UC": ["127.0.0.1:8000"],
    "RI": ["127.0.0.1:8000"]
}

while True:
    conexao, endereco = servidor.accept()
    print('Conectado por:', endereco)

    with conexao:
        while True:
            dados = conexao.recv(1024)

            if not dados:
                break

            operation = dados.decode().strip()

            if operation in servidores:
                json_resultado = json.dumps(servidores[operation])
            else:
                json_resultado = json.dumps([])

            print(f'Operação solicitada: {operation}')
            conexao.sendall(json_resultado.encode())

    print('Conexão encerrada. Aguardando nova conexão...')
    