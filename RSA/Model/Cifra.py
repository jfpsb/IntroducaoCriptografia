import io, os
from math import fmod

class Cifra:
    def __init__(self):
        self.textoClaro = ""
        self.textoCifrado = ""
        self.textoDecifrado = ""
        self.caminho = ""
        self.p = 0
        self.q = 0
        self.n = 0
        self.phi = 0
        self.chavepublica = None
        self.chaveprivada = None

    def gerarChavePublica(self):
        for e in range(3, self.phi):
            if self.mdc(e, self.phi) == 1:
                break

        self.chavepublica = (e, self.n)

        return (e, self.n)

    def gerarChavePrivada(self):
        # Gerando chave privada usando o Algoritmo Euclidiano Estendido
        # (link @ https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)
        e = self.chavepublica[0]
        r0, r1 = min(e, self.phi), max(e, self.phi)
        s0, s1 = 0, 1
        t0, t1 = 1, 0

        q = int(r0 / r1)
        r = r0 - (q * r1)
        s = s0 - (q * s1)
        t = t0 - (q * t1)

        while r != 0:
            q = int(r0 / r1)
            s = s0 - (q * s1)
            t = t0 - (q * t1)
            r = r0 - (q * r1)

            r0, r1 = r1, r
            s0, s1 = s1, s
            t0, t1 = t1, t

        while t0 < 0:
            t0 += self.phi
        
        d = t0 % self.phi

        self.chaveprivada = (d, self.n)

        return (d, self.n)

    def carregarTextoClaro(self):
        if len(self.caminho) == 0:
            raise ValueError("Escolha Um Arquivo Com Texto Claro!")

        arquivo = io.open(self.caminho, "rb")
        texto = arquivo.read()

        if len(texto.strip()) == 0:
            raise ValueError("O Arquivo Está Vazio!")

        self.textoClaro = texto

        arquivo.close()

    def cifrar(self):
        e = self.chavepublica[0]
        n = self.chavepublica[1]
        textoCifrado = ""

        for letra in self.textoClaro:
            uni_ordem = ord(letra)
            c = (uni_ordem ** e) % n
            textoCifrado += chr(c)

        self.textoCifrado = textoCifrado.strip()

    def decifrar(self):
        d = self.chaveprivada[0]
        n = self.chavepublica[1]
        textoDecifrado = ""

        for letra in self.textoCifrado:
            uni_ordem = ord(letra)
            m = (uni_ordem ** d) % n
            textoDecifrado += chr(m)

        self.textoDecifrado = textoDecifrado

    def salvarCifrado(self):
        arquivoCifrado = open(os.path.join(self.getDiretorio(), "Criptografia RSA - Texto Cifrado - " + self.getNomeArquivo()), "w")
        # Trata barra invertida
        arquivoCifrado.write(self.textoCifrado.encode("unicode-escape").decode("ascii"))

    def salvarDecifrado(self):
        arquivoDecifrado = open(os.path.join(self.getDiretorio(), "Criptografia RSA - Texto Decifrado - " + self.getNomeArquivo()), "w")
        # Trata barra invertida
        arquivoDecifrado.write(self.textoDecifrado.encode("unicode-escape").decode("ascii"))

    # Retorna diretório do arquivo contendo o texto claro
    def getDiretorio(self):
        return os.path.dirname(self.caminho)
    
    # Retorna o nome do arquivo contendo o texto claro
    def getNomeArquivo(self):
        return os.path.basename(self.caminho)

    def mdc(self, a, b):
        if a < b:
            a, b = b, a

        while b != 0:
            a, b = b, a % b

        return a