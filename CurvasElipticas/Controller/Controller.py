from Model.Cifra import Cifra
import os
from pathlib import Path

class Controller:
    def __init__(self, view):
        self.cifra = Cifra()
        self.view = view

    # Gera as chaves pública e privada
    def gerarChaves(self, p, e, d, ka, kb):
        if len(p) == 0:
            raise ValueError("Valor de P Não Pode Ser Vazio!")

        if len(e) == 0:
            raise ValueError("Valor de E Não Pode Ser Vazio!")

        if len(d) == 0:
            raise ValueError("Valor de D Não Pode Ser Vazio!")

        if len(ka) == 0:
            raise ValueError("Valor de Ka Não Pode Ser Vazio!")

        if len(kb) == 0:
            raise ValueError("Valor de Kb Não Pode Ser Vazio!")

        if not p.isdigit():
            raise ValueError("Digite Um Valor Válido Para P!")

        if not e.isdigit():
            raise ValueError("Digite Um Valor Válido Para E!")

        if not d.isdigit():
            raise ValueError("Digite Um Valor Válido Para D!")

        if not ka.isdigit():
            raise ValueError("Digite Um Valor Válido Para Ka!")

        if not kb.isdigit():
            raise ValueError("Digite Um Valor Válido Para Kb!")

        p = int(p)
        e = int(e)
        d = int(d)
        ka = int(ka)
        kb = int(kb)

        if not self.isPrime(p):
            raise ValueError("O Valor de P Precisa Ser um Número Primo!")

        self.cifra.p = p
        self.cifra.e = e
        self.cifra.d = d
        self.cifra.ka = ka
        self.cifra.kb = kb

        self.cifra.acharPontoQ()

        pubk = self.cifra.gerarChavePublica()

        self.salvarChavePublica(pubk)
        self.salvarChavePrivada((ka, kb))

        return True

    # Salva a chave pública em arquivo
    def salvarChavePublica(self, chave):
        user_dir = str(Path.home())
        arquivo = open(os.path.join(user_dir, "Criptografia de Curvas Elípticas - Chave Pública.txt"), "w")
        Ra = chave[0]
        Rb = chave[1]

        Ra.imprimir()
        Rb.imprimir()

        arquivo.write(str(Ra.x) + " " + str(Ra.y) + "\n" + str(Rb.x) + " " + str(Rb.y))
        arquivo.close()

    # Salva a chave privada em arquivo
    def salvarChavePrivada(self, chave):
        path = os.path.join(Path.home(), "Criptografia de Curvas Elípticas")
        # Cria diretório se não existir
        Path(path).mkdir(exist_ok=True)
        arquivo = open(os.path.join(path, "Criptografia de Curvas Elípticas - Chave Privada.txt"), "w")
        arquivo.write(str(chave[0]) + " " + str(chave[1]))
        arquivo.close()

    # Chama função de cifrar do modelo
    def cifrar(self):
        if len(self.cifra.caminho) == 0:
            raise ValueError("Escolha Um Arquivo Com Texto Claro!")

        if self.cifra.chaveprivada is None or self.cifra.chavepublica is None:
            raise ValueError("As Chaves Não Foram Geradas!")

        self.cifra.cifrar()

    # Chama função de decifrar do modelo
    def decifrar(self):
        self.cifra.decifrar()

    def salvarCifrado(self):
        self.cifra.salvarCifrado()

    def salvarDecifrado(self):
        self.cifra.salvarDecifrado()

    def carregarTextoClaro(self):
        self.cifra.carregarTextoClaro()

    def carregarChaves(self):
        self.cifra.carregarChaves()

    # Testa se número é primo
    def isPrime(self, n):
        if n > 1:
            for i in range(2, int(n ** 0.5) + 2):
                if n % i == 0:
                    return False
            return True
        return False

    def reset(self):
        self.cifra = Cifra()
