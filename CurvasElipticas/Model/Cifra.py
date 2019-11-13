import io
import os
import random
from pathlib import Path
from Model.Ponto import Ponto

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

        arquivo = io.open(self.caminho, "rt", encoding="utf-8")
        texto = arquivo.read()

        if len(texto.strip()) == 0:
            raise ValueError("O Arquivo Está Vazio!")

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

        chavepublica1 = publica[0].split(" ")
        chavepublica2 = publica[1].split(" ")

        self.Ra = (int(chavepublica1[0]), int(chavepublica1[1]))
        self.Rb = (int(chavepublica2[0]), int(chavepublica2[1]))
        self.ka = int(privada[0])
        self.kb = int(privada[1])

        arquivoPublica.close()
        arquivoPrivada.close()

    # Função chamada para cifrar
    def cifrar(self):
        e = self.chavepublica[0]
        n = self.chavepublica[1]
        textoCifrado = ""

        # Para cada caractere do texto claro
        for letra in self.textoClaro:
            # Pego seu valor inteiro de acordo com a tabela unicode
            uni_ordem = ord(letra)
            # Calculo o caractere criptografado
            c = (uni_ordem ** e) % n
            # Insiro no texto como uma letra da tabela unicode
            textoCifrado += chr(c)

        self.textoCifrado = textoCifrado

    # Função chamada para decifrar
    def decifrar(self):
        d = self.chaveprivada[0]
        n = self.chavepublica[1]
        textoDecifrado = ""

        # Para cada caractere do texto decifrado
        for letra in self.textoCifrado:
            # Pego seu valor inteiro de acordo com a tabela unicode
            uni_ordem = ord(letra)
            # Calculo o caractere claro
            m = (uni_ordem ** d) % n
            # Insiro no texto
            textoDecifrado += chr(m)

        self.textoDecifrado = textoDecifrado

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

    # Calcula o MDC entre dois números
    def mdc(self, a, b):
        if a < b:
            a, b = b, a

        while b != 0:
            a, b = b, a % b

        return a