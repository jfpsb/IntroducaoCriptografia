import os

class Cifra:
    def __init__(self):
        self.textoClaro = ""
        self.textoCifrado = ""
        self.textoDecifrado = ""
        self.caminho = ""
        # A chave é guardada como uma lista de pares.  O primeiro item de cada
        # par é o caractere da chave informada pelo usuário.
        # O segundo item de cada par é a posição deste caractere na chave.
        self.chave = []

    # Ordena pares de chave em relação ao caractere
    def sortChave(self):
        self.chave.sort(key = self.keyParaSort)

    # Usado na ordenação
    def keyParaSort(self, val):
        return val[0]

    # Retorna diretório do arquivo contendo o texto claro
    def getDiretorio(self):
        return os.path.dirname(self.caminho)
    
    # Retorna o nome do arquivo contendo o texto claro
    def getNomeArquivo(self):
        return os.path.basename(self.caminho)
