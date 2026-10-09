import socket

class CalculadoraRPC:

    def __init__(self, ip_servidor, porta_servidor):
        self.ip_servidor = ip_servidor
        self.porta_servidor = porta_servidor
        
        
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip_servidor, self.porta_servidor))

    def soma(self, valueA, valueB):
        return float(self.realizaOperacao("+", valueA, valueB))

    def subtracao(self, valueA, valueB):
        return float(self.realizaOperacao("-", valueA, valueB))

    def produto(self, valueA, valueB):
        return float(self.realizaOperacao("*", valueA, valueB))

    def divisao(self, valueA, valueB):
        return float(self.realizaOperacao("/", valueA, valueB))
    
    def quadrado(self, valueA):
        return float(self.realizaOperacao("**2", valueA))
    
    def upperCase(self, stri):
        return self.realizaOperacao("UC", stri)

    def redimensionar_imagem(self, src,dest,height,width):
        return self.realizaOperacao("RI", src,dest,height,width)
    
    def realizaOperacao(self, operation, valueA=None, valueB=None,option1=None,option2=None):
        mensagem = f"{operation};{valueA};{valueB};{option1};{option2}"

        self.s.sendall(mensagem.encode())
        dados = self.s.recv(1024)
        
        
        return dados.decode()
    
    
    
