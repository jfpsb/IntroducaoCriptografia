import math

class Ponto:
    def __init__(self, x, y, p, d):
        self.x = x
        self.y = y
        self.p = p
        self.d = d

    # Sobrecarregando o operador = para testar se dois pontos são iguais
    def __eq__(self, value):
        if self.x == value.x and self.y == value.y:
            return True
        return False

    # Sobrecarregando o operador aritmético + para somar dois pontos
    def __add__(self, value):
        if self.x == value.x and self.y == -value.y:
            raise ValueError("Soma é Inválida Para P = -Q")

        lbd = self.valorLambda(value)

        x = ((lbd ** 2) - self.x - value.x) % self.p
        y = ((lbd * (self.x - x)) - self.y) % self.p

        return Ponto(int(x), int(y), self.p, self.d)

    # Sobrecarregando o operador aritmético * para multiplicar um ponto por um
    # inteiro
    def __mul__(self, value):
        for i in range(value - 1):
            self += self
        return self

    # Retorna valor de lambda
    # Usando algoritmo de Gauss
    #(link @ https://math.stackexchange.com/a/174687)
    def valorLambda(self, Q):
        if self == Q:
            dividendo = 3 * (self.x ** 2) + self.d
            divisor  = 2 * self.y
        else:
            dividendo = Q.y - self.y
            divisor = Q.x - self.x

        while divisor != 1:
            if divisor < self.p:
                q = math.ceil(self.p / divisor)
                dividendo *= q
                divisor *= q

            dividendo %= self.p
            divisor %= self.p

        return dividendo

    # Imprime valores do ponto
    def imprimir(self):
        output = "Ponto: ({}, {})"
        print(output.format(self.x, self.y))
