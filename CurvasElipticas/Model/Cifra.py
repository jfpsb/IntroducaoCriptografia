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
        self.p = 23
        self.e = 1
        self.d = 1
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
        bitsClaro = BitArray(self.textoClaro).bin        
        #Calculo tamanho do bloco
        tamanho_bloco = self.tamanho_bloco(self.Q.p)
        zero = Ponto(0, 0, self.p, self.d)

        # Para cada bloco do texto claro
        for i in range(0, len(bitsClaro), tamanho_bloco):
            # Converto para int o caracteres binários presentes no bloco
            num = int(bitsClaro[i:i + tamanho_bloco], 2)
            # Calculo Pm usando o num e o ponto público Q
            Pm = self.Q * (num + k)
            # Calculo o membro C1 do conjunto de pontos criptografados
            c1 = self.Q * k
            # Calculo o membro C2 do conjunto de pontos criptografados
            c2 = Pm + (self.Rb * k)
            # Adiciono em uma variável parcial os pontos C1 e C2 separados por espaço.
            # No final de cada linha eu pulo a linha com um \n
            textoCifrado += str(c1.x) + " " + str(c1.y) + " " + str(c2.x) + " " + str(c2.y) + "\n"

        # Salvo o texto cifrado no modelo
        self.textoCifrado = textoCifrado

    # Função chamada para decifrar
    def decifrar(self, k):
        # Pego as linhas com os pontos criptografados
        linhas = self.textoCifrado.splitlines()
        # Calculo o tamanho do bloco
        tamanho_bloco = self.tamanho_bloco(self.Q.p)
        # Variável que vai guardar parciais do texto decifrado
        textoDecifrado = ""
        zero = Ponto(0, 0, self.p, self.d)

        # Para cada linha do texto cifrado
        for linha in linhas:
            # Recupero os pontos de cada linha, separados por espaço
            vals = linha.split()
            # Crio o ponto c1
            c1 = Ponto(int(vals[0]), int(vals[1]), self.Ra.p, self.Ra.d)
            # Crio o ponto c2
            c2 = Ponto(int(vals[2]), int(vals[3]), self.Ra.p, self.Ra.d)

            # Calculo o ponto Pm usando a chave privada de B
            Pm = c2 - (c1 * self.kb)

            inteiroEncontrado = False

            # Testo cada valor até p, multiplicando por pelo ponto público Q até encontrar um ponto igual a Pm.
            # O inteiro resultante é o valor inteiro do bloco que foi criptografado
            for i in range(1, tamanho_bloco ** 2):
                p = self.Q * (i + k)
                if Pm == p:
                    inteiroEncontrado = True
                    break

            if not inteiroEncontrado:
                i = 0

            # Converto número encontrado em binário
            binario = BitArray(bin(i)).bin

            # Adiciono caracteres 0 no início do número binário se houver necessidade
            for i in range(0, tamanho_bloco - len(binario)):
                binario = "0" + binario

            # Guardo resultado parcial
            textoDecifrado += binario

        for i in range(0, len(textoDecifrado), 8):
            self.textoDecifrado += chr(int(textoDecifrado[i:i+8], 2))

    def salvarCifrado(self):
        arquivoCifrado = open(os.path.join(self.getDiretorio(), "Criptografia de Curvas Elípticas - Texto Cifrado - " + self.getNomeArquivo()), "w")
        # Trata barra invertida
        arquivoCifrado.write(self.textoCifrado)

    def salvarDecifrado(self):
        arquivoDecifrado = open(os.path.join(self.getDiretorio(), "Criptografia de Curvas Elípticas - Texto Decifrado - " + self.getNomeArquivo()), "w")
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