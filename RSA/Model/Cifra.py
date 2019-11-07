import io, os, random
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
        while(True):
            # Determina e com números pseudo aleatórios
            e = random.randrange(3, self.phi)
            # Se o MDC entre e e phi for 1 então é uma chave pública válida
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

        # Se der um valor negativo somo com o phi e depois calculo o módulo
        while t0 < 0:
            t0 += self.phi
        
        d = t0 % self.phi

        self.chaveprivada = (d, self.n)

        return (d, self.n)

    def carregarTextoClaro(self):
        if len(self.caminho) == 0:
            raise ValueError("Escolha Um Arquivo Com Texto Claro!")

        arquivo = io.open(self.caminho, "rt", encoding="utf-8")
        texto = arquivo.read()

        if len(texto.strip()) == 0:
            raise ValueError("O Arquivo Está Vazio!")

        self.textoClaro = texto

        arquivo.close()

    def cifrar(self):
        e = self.chavepublica[0]
        n = self.chavepublica[1]
        textoCifrado = ""

        # Para letra do texto claro
        for letra in self.textoClaro:
            # Pego seu valor inteiro de acordo com a tabela unicode
            uni_ordem = ord(letra)
            # Calculo o caractere criptografado
            c = (uni_ordem ** e) % n
            # Insiro no texto como uma letra da tabela unicode
            textoCifrado += chr(c)

        self.textoCifrado = textoCifrado

    def decifrar(self):
        d = self.chaveprivada[0]
        n = self.chavepublica[1]
        textoDecifrado = ""

        # Para letra do texto decifrado
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