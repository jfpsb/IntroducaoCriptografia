class Ponto:
    def __init__(self, x, y, p, d):
        self.x = x
        self.y = y
        self.p = p
        self.d = d

    def __eq__(self, value):
        if self.x == value.x and self.y == value.y:
            return True
        return False

    def __add__(self, value):
        lbd = self.valorLambda(self, value)

        x = ((lbd ** 2) - self.x - value.x) % self.p
        y = (lbd*(self.x - x) - self.y) % self.p

        return Ponto(x, y, self.p, self.d)

    def __mul__(self, value):
        for i in range(value):
            self += self
        return self

    def __rmul__(self, value):
        for i in range(self):
            value += value
        return value

    def valorLambda(self, P, Q):
        if P == Q:
            return (3 * (P.x ** 2) + self.d) / (2 * P.y)
        else:
            return (Q.y - P.y) / (Q.x - P.x)

    def imprimir(self):
        output = "Ponto: ({}, {})"
        print(output.format(self.x, self.y))
