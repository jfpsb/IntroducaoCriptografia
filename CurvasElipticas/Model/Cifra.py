import io
import os
import random
from pathlib import Path
from Model.Ponto import Ponto
from bitstring import BitArray

class Cifra:
    def __init__(self):
        # Diretório onde fica a chave privada
        path = os.path.join(Path.home(), "Criptografia de Curvas Elípticas")

        self.textoClaro = ""
        self.textoCifrado = ""
        self.textoDecifrado = ""
        self.caminho = ""
        self.caminhoChavePublica = os.path.join(Path.home(), "Criptografia de Curvas Elípticas - Chave Pública.txt")
        self.caminhoChavePrivada = os.path.join(path, "Criptografia de Curvas Elípticas - Chave Privada.txt")
        self.p = 0
        self.e = 0
        self.d = 0
        self.Q = None
        self.ka = 0
        self.kb = 0
        self.Ra = None
        self.Rb = None

    # Retorna se o módulo da equação retorna zero.  Se retornar zero então os
    # valores nos dois lados da equação são iguais
    def moduloEquacao(self, x, y):
        result = ((y ** 2) - (x ** 3) - (self.d * x) - self.e)

        while result < 0:
            result += self.p

        return result % self.p == 0


    # Encontra o ponto Q presente na curva de forma pseudo aleatória
    def acharPontoQ(self):
        while True:
            x = random.randrange(0, self.p)
            y = random.randrange(0, self.p)
            if self.moduloEquacao(x, y):
                self.Q = Ponto(x, y, self.p, self.d)
                break

    # Gera a chave pública
    def gerarChavePublica(self):
        Ra = self.Q * self.ka
        Rb = self.Q * self.kb
        return (Ra, Rb)

    # Carrego texto claro no modelo
    def carregarTextoClaro(self):
        if len(self.caminho) == 0:
            raise ValueError("Escolha Um Arquivo Com Texto Claro!")

        arquivo = io.open(self.caminho, "rb")
        texto = arquivo.read()

        if len(texto.strip()) == 0:
            raise ValueError("O Arquivo Está Vazio!")

        # Espaços são substituídos pela letra X e o texto inteiro é colocado em maiúsculo
        self.textoClaro = texto

        arquivo.close()

    # Carrego as chaves de seus arquivos
    def carregarChaves(self):
        arquivoPublica = io.open(self.caminhoChavePublica, "rt")
        arquivoPrivada = io.open(self.caminhoChavePrivada, "rt")
        publica = arquivoPublica.read()
        privada = arquivoPrivada.read()

        if len(publica.strip()) == 0:
            raise ValueError("A Chave Pública Está Vazia!")

        if len(privada.strip()) == 0:
            raise ValueError("A Chave Privada Está Vazia!")

        publica = publica.splitlines()
        privada = privada.split(" ")

        valorQ = publica[0].split(" ")
        chavepublica1 = publica[1].split(" ")
        chavepublica2 = publica[2].split(" ")

        self.Q = Ponto(int(valorQ[0]), int(valorQ[1]), int(valorQ[2]), int(valorQ[3]))
        self.Ra = Ponto(int(chavepublica1[0]), int(chavepublica1[1]), int(chavepublica1[2]), int(chavepublica1[3]))
        self.Rb = Ponto(int(chavepublica2[0]), int(chavepublica2[1]), int(chavepublica1[2]), int(chavepublica1[3]))
        self.ka = int(privada[0])
        self.kb = int(privada[1])

        arquivoPublica.close()
        arquivoPrivada.close()

    # Função chamada para cifrar
    # De A para B
    def cifrar(self, k):
        textoCifrado = ""

        # Pego a representção do texto em binário
        bytesClaro = BitArray(self.textoClaro).bin        
        #Calculo tamanho do bloco
        tamanho_bloco = self.tamanho_bloco(self.Q.p)

        for i in range(0, len(bytesClaro), tamanho_bloco):
            num = int(bytesClaro[i:i + tamanho_bloco], 2)
            Pm = self.Q * num
            Pm.imprimir()
            c1 = self.Q * k
            c2 = Pm + (self.Rb * k)
            # Insiro no texto como uma letra da tabela unicode
            textoCifrado += str(c1.x) + " " + str(c1.y) + " " + str(c2.x) + " " + str(c2.y) + "\n"

        # Para cada caractere do texto claro
        #for letra in self.textoClaro:
        #    # Pego seu valor inteiro de acordo com a tabela unicode
        #    uni_ordem = ord(letra)
        #    # Uso este valor para achar o ponto Pm na curva
        #    Pm = self.Q * uni_ordem
        #    # Calculo o caractere criptografado
        #    c1 = self.Q * k
        #    c2 = Pm + (self.Rb * k)
        #    # Insiro no texto como uma letra da tabela unicode
        #    textoCifrado += str(c1.x) + " " + str(c1.y) + " " + str(c2.x) + " " + str(c2.y) + "\n"

        self.textoCifrado = textoCifrado

    # Função chamada para decifrar
    def decifrar(self):
        linhas = self.textoCifrado.splitlines()
        tamanho_bloco = self.tamanho_bloco(self.Q.p)
        textoDecifrado = ""

        for linha in linhas:
            vals = linha.split()
            c1 = Ponto(int(vals[0]), int(vals[1]), self.Ra.p, self.Ra.d)
            c2 = Ponto(int(vals[2]), int(vals[3]), self.Ra.p, self.Ra.d)

            Pm = c2 - (c1 * self.kb)

            for i in range(0, self.Q.p):
                p = self.Q * i
                if Pm == p:
                    print("--")
                    Pm.imprimir()
                    break

            binario = bin(i)[2:]

            for i in range(0, tamanho_bloco - len(binario)):
                binario = "0" + binario

            textoDecifrado += binario

        for i in range(0, len(textoDecifrado), 8):
            self.textoDecifrado += chr(int(textoDecifrado[i:i+8], 2))

    def salvarCifrado(self):
        arquivoCifrado = open(os.path.join(self.getDiretorio(), "Criptografia RSA - Texto Cifrado - " + self.getNomeArquivo()), "w")
        # Trata barra invertida
        arquivoCifrado.write(self.textoCifrado.encode("unicode-escape").decode("ascii"))

    def salvarDecifrado(self):
        arquivoDecifrado = open(os.path.join(self.getDiretorio(), "Criptografia RSA - Texto Decifrado - " + self.getNomeArquivo()), "w")
        arquivoDecifrado.write(self.textoDecifrado)

    # Retorna diretório do arquivo contendo o texto claro
    def getDiretorio(self):
        return os.path.dirname(self.caminho)
    
    # Retorna o nome do arquivo contendo o texto claro
    def getNomeArquivo(self):
        return os.path.basename(self.caminho)

    def tamanho_bloco(self, p):
        for blockSize in range(0, p):
            if 2 ** (blockSize + 1) > p:
                break
        return blockSize