import socket
from PIL import Image
import os

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('127.0.0.1', 8000))
servidor.listen()
print('Aguardando conexao...')

conexao, endereco = servidor.accept()
with conexao:
    print('Conectado por:', endereco)
    while True:
        dados = conexao.recv(1024)
        if not dados:  
            break
            
        mensagem = dados.decode()
        
        partes = mensagem.split(";")
        operation = partes[0]
        
        valor = 0
        if operation == "+":
            valor = float(partes[1]) + float(partes[2])
        elif operation == "-":
            valor = float(partes[1]) - float(partes[2])
        elif operation == "/":
            try:
                valor = float(partes[1]) / float(partes[2])
            except ZeroDivisionError:
                valor=0
        elif operation == "*":
            valor = float(partes[1]) * float(partes[2])
        elif operation == "**2":
            valor = float(partes[1])**2
        elif operation == "UC":
            valor = partes[1].upper()
        elif operation == "RI":
            try:
                imagem = Image.open(partes[1])
                imagem_redimensionada = imagem.resize((int(partes[3]), int(partes[4])))
                imagem_redimensionada.save(partes[2])
                valor=os.path.getsize(partes[2])
            except FileNotFoundError:
                valor = 0

            except UnidentifiedImageError:
                valor = 0

            except PermissionError:
                valor = 0

            except (OSError, ValueError) as erro:
                valor = 0
        else:
            valor = 0

        
        conexao.sendall(str(valor).encode())
