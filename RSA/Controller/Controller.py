from Model.Cifra import Cifra

class Controller:
    def __init__(self):
        self.cifra = Cifra()

    def gerarChaves(self, p, q):
        self.cifra.p = p
        self.cifra.q = q
        self.cifra.n = p * q
