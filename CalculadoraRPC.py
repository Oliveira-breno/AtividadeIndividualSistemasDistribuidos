import socket
import random
import json

class CalculadoraRPC:

    def __init__(self, ip_servidor_nome, porta_servidor_nome):
        self.ip_servidor_nome = ip_servidor_nome
        self.porta_servidor_nome = porta_servidor_nome
        
        
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip_servidor_nome, self.porta_servidor_nome))

    def soma(self, valueA, valueB):
        end = self.descobreEndereco("+")
        return float(self.realizaOperacao(end,"+", valueA, valueB))

    def subtracao(self, valueA, valueB):
        end = self.descobreEndereco("-")
        return float(self.realizaOperacao(end,"-", valueA, valueB))

    def produto(self, valueA, valueB):
        end = self.descobreEndereco("*")
        return float(self.realizaOperacao(end,"*", valueA, valueB))

    def divisao(self, valueA, valueB):
        end = self.descobreEndereco("/")
        return float(self.realizaOperacao(end,"/", valueA, valueB))
    
    def quadrado(self, valueA):
        end = self.descobreEndereco("**2")
        return float(self.realizaOperacao(end,"**2", valueA))
    
    def upperCase(self, stri):
        end = self.descobreEndereco("UC")
        return self.realizaOperacao(end,"UC", stri)

    def redimensionar_imagem(self, src,dest,height,width):
        end = self.descobreEndereco("RI")
        return self.realizaOperacao(end,"RI", src,dest,height,width)

    def listarJson(self,mensagem):
        return json.loads(mensagem)
    

    def sorteiaIP(self,lista):
        indice_sorteado = random.randint(0, len(lista) - 1)
        print(indice_sorteado)
        return lista[indice_sorteado]

    def descobreEndereco(self,operation):
        mensagem=f"{operation}"

        self.s.sendall(mensagem.encode())
        dados = self.s.recv(1024)
        lista=self.listarJson(dados.decode())
        end = self.sorteiaIP(lista)
        return end

    
    def realizaOperacao(self,end,operation, valueA=None, valueB=None,option1=None,option2=None):
        mensagem = f"{operation};{valueA};{valueB};{option1};{option2}"

        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.connect((end.split(":")[0],int(end.split(":")[1])))
        sk.sendall(mensagem.encode())
        dados = sk.recv(1024)
        
        sk.close()
        
        return dados.decode()
    
    
    
