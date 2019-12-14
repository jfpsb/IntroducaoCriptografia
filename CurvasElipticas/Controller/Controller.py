from Model.Cifra import Cifra
import os
from pathlib import Path

class Controller:
    def __init__(self, view):
        self.cifra = Cifra()
        self.view = view

    # Gera as chaves pública e privada
    def gerarChaves(self, ka, kb):
        if len(ka) == 0:
            raise ValueError("Valor de Ka Não Pode Ser Vazio!")

        if len(kb) == 0:
            raise ValueError("Valor de Kb Não Pode Ser Vazio!")

        if not ka.isdigit():
            raise ValueError("Digite Um Valor Válido Para Ka!")

        if not kb.isdigit():
            raise ValueError("Digite Um Valor Válido Para Kb!")

        ka = int(ka)
        kb = int(kb)

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

        arquivo.write(str(self.cifra.Q.x) + " " + str(self.cifra.Q.y) + " " + str(self.cifra.Q.p) + " " + str(self.cifra.Q.d) + "\n")
        arquivo.write(str(Ra.x) + " " + str(Ra.y) + " " + str(Ra.p) + " " + str(Ra.d) +"\n")
        arquivo.write(str(Rb.x) + " " + str(Rb.y) + " " + str(Rb.p) + " " + str(Rb.d))
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
    def cifrar(self, k):
        if len(k) == 0:
            raise ValueError("Informe Um Valor Para K!")

        if not k.isdigit():
            raise ValueError("Informe Um Valor Válido Para K!")

        if len(self.cifra.caminho) == 0:
            raise ValueError("Escolha Um Arquivo Com Texto Claro!")

        if self.cifra.Ra is None or self.cifra.Rb is None:
            raise ValueError("As Chaves Não Foram Geradas!")

        k = int(k)

        self.cifra.cifrar(k)

    # Chama função de decifrar do modelo
    def decifrar(self, k):
        self.cifra.decifrar(int(k))

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

