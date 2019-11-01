class Cifra:
    def __init__(self):
        self.p = 0
        self.q = 0
        self.n = 0

    def phi(self):
        return (p - 1) * (q - 1)

    def mdc(self, a, b):
        if a == b:
            return a

        if a < b:
            a, b = b, a

        while b != 0:
            a, b = b, a % b

        return a
