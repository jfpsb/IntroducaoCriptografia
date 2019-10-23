import random
from model.Node import Node

# Engrenagem é uma lista circular
class Engrenagem:
    def __init__(self):
        self.cabeca = None
        self.fim = None
        self.proximaEngrenagem = None
        self.tamanho = 0
        self.rotacionado = 0

        self.caracteres = []

        # Adicionando os caracteres do alfabeto da engrenagem.
        # Começando do 32, igual ao espaço na tabela unicode
        # até o 255, igual a ÿ na tabela unicode.
        # Ao todo são 191 caracteres 'printáveis' com suporte
        for i in range(32, 256):
            self.caracteres.append(chr(i))

        #random.shuffle(numeros)

        for i in self.caracteres:
            self.add(i)

    def add(self, caractere):
        # Cria node
        node = Node(caractere)
        # Se for o primeiro item sendo adicionado
        if self.tamanho == 0:
            self.cabeca = node
            self.fim = node
            node.proximoNode = node
        else:
            node.proximoNode = self.cabeca
            self.fim.proximoNode = node
            self.fim = node
        # Incrementa tamanho da lista circular
        self.tamanho += 1

    # Recupera node baseado no caractere informado
    def get(self, caractere):
        temp = None

        if self.cabeca is not None:
            temp = self.cabeca
            aux = 32 # Início da numeração do alfabeto na tabela unicode
            # Itera o número de vezes que o caractere representa na tabela unicode.
            # Exemplo: 'a' na tabela é representada pelo número 97.
            # A lista circular será iterada 97 - 32 = 65 vezes a partir da cabeça.
            while aux < ord(caractere):
                temp = temp.proximoNode
                aux += 1

        return temp

    # Rotaciona os itens da engrenagem
    def rotacionar(self):
        temp = None
        if self.cabeca is not None:
            # Recupera o antepenultimo item da lista circular
            temp = self.cabeca
            while temp.proximoNode is not self.fim:
                temp = temp.proximoNode

            # Realiza a rotação somente mudando a atribuição de cabeça e fim da lista
            antPenultimoNode = temp
            self.cabeca = self.fim
            self.fim = antPenultimoNode

            self.rotacionado += 1

            # Se engrenagem realizar uma revolução completa, rotaciona a próxima engrenagem uma vez
            if self.rotacionado == len(self.caracteres):
                self.rotacionado = 0
                self.proximaEngrenagem.rotacionar()

    # Limpa itens da lista circular
    def clear(self):
        self.cabeca = None
        self.fim = None
        self.tamanho = 0
        self.rotacionado = 0

    # Restaura lista para estado inicial
    def reset(self):
        self.clear()
        for i in self.caracteres:
            self.add(i)