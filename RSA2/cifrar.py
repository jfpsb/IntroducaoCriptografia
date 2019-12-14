import os, io
from bitstring import BitArray

class Cifrar:
    def __init__(self):
        self.textoCifrado = ""
        self.textoClaro = self.carregarTextoClaro()
        self.chavePublica = self.carregaChavePublica()
        self.cifrar()
        self.salvarCifrado()

    # Carrego texto claro de arquivo
    def carregarTextoClaro(self):
        arquivo = io.open("claro.txt", "rb")
        texto = arquivo.read()
        arquivo.close()
        return texto

    # Função de cifragem
    def cifrar(self):
        e = self.chavePublica[0]
        n = self.chavePublica[1]
        # Variável parcial para guardar texto cifrado
        textoCifrado = ""

        # Pego a representação do texto claro em binário
        bitsClaro = BitArray(self.textoClaro).bin
        # Tamanho do bloco de dados baseado no valor de n
        tamanho_bloco = self.tamanho_bloco(n)

        # Para cada bloco do texto claro
        for i in range(0, len(bitsClaro), tamanho_bloco):
            # Recupero os bits do bloco
            bloco = bitsClaro[i:i + tamanho_bloco]
            # Se o bloco recuperado for menor, em bits, que o tamanho do bloco de dados, adiciono zeros no final
            if len(bloco) < tamanho_bloco:
                for i in range(0, tamanho_bloco - len(bloco)):
                    bloco += "0"
            # Converto o bloco para inteiro
            num = int(bloco, 2)
            # Calculo o valor do bloco criptografado
            c = (num ** e) % n
            # Adiciono na variável parcial o caractere que representa cada bloco de acordo com a tabela unicode.
            # chr(127) retorna um caractere da tabela unicode que estou usando como delimitador entre os caracteres que calculei.
            textoCifrado += chr(c) + chr(127)

        # Salvo o texto cifrado encontrado.
        # O caracteres encontrados são salvos em texto
        self.textoCifrado = textoCifrado

    # Carrego a chave pública de seu arquivo
    def carregaChavePublica(self):
        pu = io.open("pu.txt", "rt")
        chavePublica = pu.read()
        # A chave são dois valores separados por um espaço
        chavePublica = chavePublica.split()
        pu.close()
        return (int(chavePublica[0]), int(chavePublica[1]))

    def salvarCifrado(self):
        arquivo = open("c.txt", "w", encoding="utf-8")
        # Alguns caracteres da tabela unicode não tem representação textual, então no arquivo eles ficam
        # com uma barra invertida. Exemplo: \xC2. Para salvar texto com barra invertida preciso usar encode
        # e depois decode em ascii para salvar no txt
        arquivo.write(self.textoCifrado.encode("unicode-escape").decode("ascii"))
        arquivo.close()

    # Retorna tamanho do bloco
    def tamanho_bloco(self, p):
        for blockSize in range(0, p):
            if 2 ** (blockSize + 1) > p:
                break
        return blockSize
