import io, os, re
from Cifra import Cifra
from Engrenagem import Engrenagem
from Node import Node

class Controller:
    def __init__(self):
        self.cifra = Cifra()
        self.inicializaEngrenagem()

    def cifrar(self):
        textoCifrado = ""

        # Para cada letra no texto claro
        for i in self.cifra.textoClaro:
            # Retorna node correspondente à letra informada
            node1 = self.engrenagem1.get(i)
            node2 = self.engrenagem2.get(node1.caractere)
            node3 = self.engrenagem3.get(node2.caractere)

            # Rotaciona engrenagem 1
            self.engrenagem1.rotacionar()

            # Guarda caractere resultante em variável parcial
            textoCifrado += node3.caractere

        self.cifra.textoCifrado = textoCifrado

    def decifrar(self):
        textoCifrado = self.cifra.textoCifrado
        textoDecifrado = ""

        # Reinicia as engrenagens para configuração inicial
        self.engrenagem1.reset()
        self.engrenagem2.reset()
        self.engrenagem3.reset()

        # Para cada letra do texto cifrado
        for i in textoCifrado:
            # Para cada letra do alfabeto
            for j in self.engrenagem1.caracteres:
                # Informa a letra e retorna node
                node1 = self.engrenagem1.get(j)
                node2 = self.engrenagem2.get(node1.caractere)
                node3 = self.engrenagem3.get(node2.caractere)

                # Se node resultante tiver o mesmo caractere do texto cifrado
                # adicionar ao texto decifrado e rotacionar engrenagem 1
                if node3.caractere == i:
                    self.engrenagem1.rotacionar()
                    textoDecifrado += j
                    break

        self.cifra.textoDecifrado = textoDecifrado

    def salvarCifrado(self):
        arquivoCifrado = open(os.path.join(self.cifra.getDiretorio(), "Ativ. Individual 2 - Máquina de Rotação - Texto Cifrado - " + self.cifra.getNomeArquivo()), "w")
        # Trata barra invertida
        arquivoCifrado.write(self.cifra.textoCifrado.encode("unicode-escape").decode("ascii"))

    def salvarDecifrado(self):
        arquivoDecifrado = open(os.path.join(self.cifra.getDiretorio(), "Ativ. Individual 2 - Máquina de Rotação - Texto Decifrado - " + self.cifra.getNomeArquivo()), "w")
        # Trata barra invertida
        arquivoDecifrado.write(self.cifra.textoDecifrado.encode("unicode-escape").decode("ascii"))

    # Lê texto claro de arquivo
    def leTextoClaro(self):
        if len(self.cifra.caminho) == 0:
            raise ValueError("Escolha Um Arquivo Com Texto Claro!")

        arquivo = io.open(self.cifra.caminho, "rt", encoding="utf-8")
        texto = arquivo.read()

        if len(texto.strip()) == 0:
            raise ValueError("O Arquivo Está Vazio!")

        self.cifra.textoClaro = texto
        arquivo.close()

    def inicializaEngrenagem(self):
        self.engrenagem1 = Engrenagem()
        self.engrenagem2 = Engrenagem()
        self.engrenagem3 = Engrenagem()

        self.engrenagem1.proximaEngrenagem = self.engrenagem2
        self.engrenagem2.proximaEngrenagem = self.engrenagem3
        self.engrenagem3.proximaEngrenagem = self.engrenagem1

    def reset(self):
        self.cifra = Cifra()
        self.inicializaEngrenagem()
