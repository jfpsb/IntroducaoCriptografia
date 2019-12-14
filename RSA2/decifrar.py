import os
import io
import unicodedata
from bitstring import BitArray

class Decifrar:
    def __init__(self):
        self.textoDecifrado = ""
        self.textoCifrado = self.carregarTextoCifrado()
        self.chavePrivada = self.carregaChavePrivada()
        self.decifrar()
        self.salvarDecifrado()

    # Carrego texto claro de arquivo
    def carregarTextoCifrado(self):
        arquivo = io.open("c.txt", "rb")
        texto = arquivo.read().decode('unicode_escape')
        arquivo.close()
        return texto

    # Função para decifrar
    def decifrar(self):
        d = self.chavePrivada[0]
        n = self.chavePrivada[1]
        # Variável parcial para guardar texto decifrado
        textoDecifrado = ""

        # Cada caractere no texto cifrado representa um bloco do texto claro.
        # Aqui eu separo cada caractere pelo delimitador que usei na cifragem (chr(127))
        caracteres = self.textoCifrado.split(chr(127))
        tamanho_bloco = self.tamanho_bloco(n)

        # Para cada caractere
        for caractere in caracteres:
            # Se por acaso algum caractere tiver tamanho zero, é ignorado
            if len(caractere) == 0:
                continue
            # Recupero o número que esse caractere representa na tabela unicode.
            num = ord(caractere)
            # DEC é igual ao número que representa o bloco no texto claro
            dec = (num ** d) % n
            # DECBIN guarda DEC representado em binário
            decbin = BitArray(bin(dec)).bin
            # Se DECBIN for menor que o tamanho do bloco,
            # adiciono zeros no início dele para completar até o tamanho do bloco
            if len(decbin) < tamanho_bloco:
                padding = ""
                for i in range(0, tamanho_bloco - len(decbin)):
                    padding += "0"
                decbin = padding + decbin
            # Guardo DECBIN na variável parcial
            textoDecifrado += decbin

        # Cada caractere em um texto são 8 bits, então divido o binário que encontrei em blocos de 8 bits.
        # Cada bloco de 8 bits representa uma letra.
        for i in range(0, len(textoDecifrado), 8):
            # Converto o bloco de 8 bits para inteiro
            chr_ordem = int(textoDecifrado[i:i + 8], 2)
            # Recupero o caractere de acordo com a tabela unicode usando função chr.
            # Adiciono no texto decifrado
            self.textoDecifrado += chr(chr_ordem)

    # Carrego a chave privada de seu arquivo
    def carregaChavePrivada(self):
        pr = io.open("pr.txt", "rt")
        chavePrivada = pr.read()
        # A chave são dois valores separados por um espaço
        chavePrivada = chavePrivada.split()
        pr.close()
        return (int(chavePrivada[0]), int(chavePrivada[1]))

    def salvarDecifrado(self):
        arquivo = open("d.txt", "w")
        arquivo.write(self.textoDecifrado)

    # Retorna tamanho do bloco
    def tamanho_bloco(self, p):
        for blockSize in range(0, p):
            if 2 ** (blockSize + 1) > p:
                break
        return blockSize
