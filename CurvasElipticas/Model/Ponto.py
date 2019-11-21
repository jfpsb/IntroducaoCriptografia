import math

class Ponto:
    def __init__(self, x, y, p, d):
        self.x = x
        self.y = y
        self.p = p
        self.d = d

    # Sobrecarregando o operador == para testar se dois pontos são iguais
    def __eq__(self, value):
        if self.x == value.x and self.y == value.y:
            return True
        return False

    # Sobrecarregando o operador aritmético + para somar dois pontos
    def __add__(self, value):
        if self.x == value.x and self.y == -value.y:
            return self

        lbd = self.valorLambda(value)

        if not lbd:
            return self

        x = ((lbd ** 2) - self.x - value.x) % self.p
        y = (lbd * (self.x - x) - self.y) % self.p

        return Ponto(int(x), int(y), self.p, self.d)

    # Sobrecarregando o operador aritmético - para subtrair dois pontos
    def __sub__(self, value):
        p = Ponto(value.x, -value.y, value.p, value.d)
        return self + p

    # Sobrecarregando o operador aritmético * para multiplicar um ponto por um
    # inteiro
    def __mul__(self, value):
        pontoinicial = Ponto(self.x, self.y, self.p, self.d)
        for i in range(value - 1):
            self += pontoinicial
        return self

    # Sobrecarregando o operador aritmético * para multiplicar um inteiro por um
    # ponto
    def __rmul__(self, value):
        for i in range(self - 1):
            value += value
        return value

    # Retorna valor de lambda
    def valorLambda(self, Q):
        if self == Q:
            if self.y == 0:
                return False
            dividendo = 3 * (self.x ** 2) + self.d
            divisor  = 2 * self.y
        else:
            if Q.x == self.x:
                return False
            dividendo = Q.y - self.y
            divisor = Q.x - self.x

        return (dividendo * self.fermat(divisor, self.p)) % self.p

    # Imprime valores do ponto
    def imprimir(self):
        output = "Ponto: ({}, {})"
        print(output.format(self.x, self.y))

    # Usando teorema pequeno de Fermat para calcular módulo inverso
    def fermat(self, a, p):
        if p - 2 == 0:
            return 1
        return (a ** (p - 2)) % p

    # Calcula o MDC entre dois números
    def mdc(self, a, b):
        if a < b:
            a, b = b, a

        while b != 0:
            a, b = b, a % b

        return a
