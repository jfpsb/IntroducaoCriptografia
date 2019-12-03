from Cifra import Cifra
import os
from pathlib import Path

class Controller:
    def __init__(self, view):
        self.cifra = Cifra()
        self.view = view

    # Gera as chaves pública e privada
    def gerarChaves(self, p, q):
        if len(p) == 0:
            raise ValueError("Valor de P Não Pode Ser Vazio!")

        if len(q) == 0:
            raise ValueError("Valor de Q Não Pode Ser Vazio!")

        if not p.isdigit():
            raise ValueError("Digite Um Valor Válido Para P!")

        if not q.isdigit():
            raise ValueError("Digite Um Valor Válido Para Q!")

        p = int(p)
        q = int(q)

        if not self.isPrime(p):
            raise ValueError("O Valor de P Precisa Ser um Número Primo!")

        if not self.isPrime(q):
            raise ValueError("O Valor de Q Precisa Ser um Número Primo!")

        if p * q < 256:
            raise ValueError("O Valor do Módulo Precisa Ser Maior Que 256")

        self.cifra.p = p
        self.cifra.q = q
        self.cifra.n = p * q
        self.cifra.phi = (p - 1) * (q - 1)

        pubk = self.cifra.gerarChavePublica()
        privk = self.cifra.gerarChavePrivada(pubk[0])

        self.salvarChavePublica(pubk)
        self.salvarChavePrivada(privk)

        return True

    # Salva a chave pública em arquivo
    def salvarChavePublica(self, chave):
        user_dir = str(Path.home())
        arquivo = open(os.path.join(user_dir, "Criptografia RSA - Chave Pública.txt"), "w")
        arquivo.write(str(chave[0]) + " " + str(chave[1]))
        arquivo.close()

    # Salva a chave privada em arquivo
    def salvarChavePrivada(self, chave):
        path = os.path.join(Path.home(), "Criptografia RSA")
        # Cria diretório se não existir
        Path(path).mkdir(exist_ok=True)
        arquivo = open(os.path.join(path, "Criptografia RSA - Chave Privada.txt"), "w")
        arquivo.write(str(chave[0]) + " " + str(chave[1]))
        arquivo.close()

    # Chama função de cifrar do modelo
    def cifrar(self):
        if len(self.cifra.caminho) == 0:
            raise ValueError("Escolha Um Arquivo Com Texto Claro!")

        if self.cifra.chaveprivada is None or self.cifra.chavepublica is None:
            raise ValueError("As Chaves Não Foram Geradas!")

        self.cifra.cifrar()

    # Chama função de decifrar do modelo
    def decifrar(self):
        self.cifra.decifrar()

    def salvarCifrado(self):
        self.cifra.salvarCifrado()

    def salvarDecifrado(self):
        self.cifra.salvarDecifrado()

    def carregarTextoClaro(self):
        self.cifra.carregarTextoClaro()

    def carregarChaves(self):
        self.cifra.carregarChaves()

    # Testa se número é primo
    def isPrime(self, n):
        if n > 1:
            for i in range(2, int(n**0.5) + 2):
                if n % i == 0:
                    return False
            return True
        return False

    def reset(self):
        self.cifra = Cifra()

