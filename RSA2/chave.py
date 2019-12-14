import os

class Chave:
    def __init__(self):
        while True:
            print("Informe Os Valores de P, Q e E (separados por espaço):")
            pqe = input().split()
            self.p = int(pqe[0])
            self.q = int(pqe[1])
            self.e = int(pqe[2])

            # Se P não for primo
            if not self.isPrime(self.p):
                print("P Precisa Ser Primo")
                continue

            # Se Q não for primo
            if not self.isPrime(self.q):
                print("Q Precisa Ser Primo")
                continue

            self.n = self.p * self.q
            self.phi = (self.p - 1) * (self.q - 1)

            # E precisa ser menor que PHI
            if self.e >= self.phi:
                print("O Valor de E Deve Ser Menor que PHI")
                continue

            # E e PHI precisam ser primos entre si
            if self.mdc(self.e, self.phi) != 1:
                print("O MDC entre E e PHI é diferente de 1. A Chave Pública É Inválida")
                continue

            self.chavePublica = (self.e, self.n)
            self.chavePrivada = self.gerarChavePrivada(self.e)

            diretorioAtual = os.getcwd()

            # Salvando chaves em arquivo
            arquivo = open(os.path.join(diretorioAtual, "pu.txt"), "w")
            arquivo.write(str(self.chavePublica[0]) + " " + str(self.chavePublica[1]))
            arquivo.close()

            arquivo = open(os.path.join(diretorioAtual, "pr.txt"), "w")
            arquivo.write(str(self.chavePrivada[0]) + " " + str(self.chavePrivada[1]))
            arquivo.close()

            break

    # Gera a chave privada
    def gerarChavePrivada(self, e):
        # Gerando chave privada usando o Algoritmo Euclidiano Estendido
        # (link @ https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)
        r0, r1 = min(e, self.phi), max(e, self.phi)
        s0, s1 = 0, 1
        t0, t1 = 1, 0

        q = int(r0 / r1)
        r = r0 - (q * r1)
        s = s0 - (q * s1)
        t = t0 - (q * t1)

        while r != 0:
            q = int(r0 / r1)
            s = s0 - (q * s1)
            t = t0 - (q * t1)
            r = r0 - (q * r1)

            r0, r1 = r1, r
            s0, s1 = s1, s
            t0, t1 = t1, t

        # Se der um valor negativo somo com o phi e depois calculo o módulo
        while t0 < 0:
            t0 += self.phi
        
        d = t0 % self.phi

        return (d, self.n)

    # Testa se número é primo
    def isPrime(self, n):
        if n > 1:
            for i in range(2, int(n ** 0.5) + 2):
                if n % i == 0:
                    return False
            return True
        return False

    # Calcula o MDC entre dois números
    def mdc(self, a, b):
        if a < b:
            a, b = b, a

        while b != 0:
            a, b = b, a % b

        return a
