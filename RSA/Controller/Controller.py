from Model.Cifra import Cifra

class Controller:
    def __init__(self, view):
        self.cifra = Cifra()
        self.view = view

    def gerarChaves(self, p, q):
        if len(p) == 0:
            raise ValueError("Valor de P Não Pode Ser Vazio!")

        if len(q) == 0:
            raise ValueError("Valor de Q Não Pode Ser Vazio!")

        if not p.isdigit():
            raise ValueError("Digite Um Valor Válido Para P!")

        if not q.isdigit():
            raise ValueError("Digite Um Valor Válido Para Q!")

        p = int(p)
        q = int(q)

        if not self.isPrime(p):
            raise ValueError("O Valor de P Precisa Ser um Número Primo!")

        if not self.isPrime(q):
            raise ValueError("O Valor de Q Precisa Ser um Número Primo!")

        if p * q < 256:
            raise ValueError("O Valor do Módulo Precisa Ser Maior Que 256")

        self.cifra.p = p
        self.cifra.q = q
        self.cifra.n = p * q
        self.cifra.phi = (p - 1) * (q - 1)

        pubk = self.cifra.gerarChavePublica()
        privk = self.cifra.gerarChavePrivada()

        self.view.atualizaLabelChave(pubk[0], privk[0], privk[1])

    def cifrar(self):
        if len(self.cifra.caminho) == 0:
            raise ValueError("Escolha Um Arquivo Com Texto Claro!")

        if self.cifra.chaveprivada is None or self.cifra.chavepublica is None:
            raise ValueError("As Chaves Não Foram Geradas!")

        self.cifra.cifrar()

    def decifrar(self):
        self.cifra.decifrar()

    def salvarCifrado(self):
        self.cifra.salvarCifrado()

    def salvarDecifrado(self):
        self.cifra.salvarDecifrado()

    def carregarTextoClaro(self):
        self.cifra.carregarTextoClaro()

    def isPrime(self, n):
        if n > 1:
            for i in range(2, int(n**0.5) + 2):
                if n % i == 0:
                    return False
            return True
        return False

    def reset(self):
        self.cifra = Cifra()

