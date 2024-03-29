import Cifra
import io, os

class Controller:
    def __init__(self):
        self.cifra = Cifra.Cifra()

    def cifrar(self):
        # UTILIZO O TERMO MATRIZ AQUI, MAS A MANIPULAÇÃO É FEITA EM UM VETOR

		# Se não for informado o arquivo com texto claro
        if len(self.cifra.caminho) == 0:
            raise ValueError("Escolha Um Arquivo Com Texto Claro!")

        # Guarda texto claro
        textoClaro = self.cifra.textoClaro
        # Guarda tamanho da chave
        tamanhoChave = len(self.cifra.chave)

        # Calcula quantos campos do texto claro ficam em branco se o texto
        # claro for disposto numa matriz
        # com número de colunas igual ao tamanho da chave.
        # Preenche os campos em branco com letras começando pela letra 'a'
        camposVazios = 0
        if len(textoClaro) % tamanhoChave != 0:
            camposVazios = tamanhoChave - (len(textoClaro) % tamanhoChave)

        for i in range(camposVazios):
            textoClaro += chr(97 + i) # Converte para char. 97 corresponde a 'a' na tabela unicode

        # Calcula quantas linhas teria a matriz com texto claro
        linhas = int(len(textoClaro) / tamanhoChave)

        # Guarda o texto claro na variável de texto cifrado inicialmente para
        # começar cifragem
        textoCifrado = textoClaro

        # 3 estágios de cifragem
        for i in range(3):
            # Guarda o resultado parcial da cifragem a cada estágio
            cifradoParcial = ""
            # Para cada item da chave
            for j in self.cifra.chave:
                # Pega a posição do caractere na chave, que seria o mesmo que a
                # coluna em uma matriz
                colunaAtual = j[1]
                # Para cada linha da matriz
                for k in range(linhas):
                    # Adiciona na variável que guarda a cifragem neste estágio
                    cifradoParcial += textoCifrado[colunaAtual]
                    # Adiciona o tamanho da chave para pular para a próximo
                    # letra na próxima linha da matriz
                    colunaAtual += tamanhoChave

            # Guarda o resultado da cifragem deste estágio
            textoCifrado = cifradoParcial

        # Ao fim de todos os estágios salva o texto cifrado no modelo
        self.cifra.textoCifrado = textoCifrado

    def decifrar(self):
        # UTILIZO O TERMO MATRIZ AQUI, MAS A MANIPULAÇÃO É FEITA EM UM VETOR

        # Guarda tamanho da chave
        tamanhoChave = len(self.cifra.chave)
        # Guarda o texto cifrado inicialmente na variável de texto decifrado
        # para iniciar decifragem
        textoDecifrado = self.cifra.textoCifrado
        # Calcula o número de linhas que teria na matriz
        linhas = int(len(textoDecifrado) / tamanhoChave)
        # Crio lista que vai guardar o resultado parcial da decifragem a cada
        # estágio
        decifradoParcial = [""] * len(textoDecifrado)

        # 3 estágios de decifragem
        for i in range(3):
            # Posição de par na lista de chave
            posicaoChave = 0
            # Para cada letra do texto cifrado
            for j in range(len(textoDecifrado)):
                # Condição para trocar de coluna na matriz.
                # Se no início do loop atribuir valores do primeiro par da
                # chave
                if j == 0 or (j >= linhas and (j % linhas) == 0):
                    par = self.cifra.chave[posicaoChave]
                    coluna = par[1]
                    posicaoChave += 1
                # Guarda parcial da decifragem
                decifradoParcial[coluna] = textoDecifrado[j]
                # Soma tamanho da chave no valor de coluna para pular para
                # próxima linha da matriz
                coluna += tamanhoChave
            # Guarda resultado parcial do estágio.
            # decifradoParcial é uma lista, por isso uso método join para
            # converter para string
            textoDecifrado = "".join(decifradoParcial)
        # Salva texto decifrado em modelo
        self.cifra.textoDecifrado = textoDecifrado

    def salvarCifrado(self):
        arquivoCifrado = open(os.path.join(self.cifra.getDiretorio(), "Ativ. Individual 1 - Transp. Linha x Coluna - Texto Cifrado - " + self.cifra.getNomeArquivo()), "w")
        arquivoCifrado.write(self.cifra.textoCifrado)

    def salvarDecifrado(self):
        arquivoDecifrado = open(os.path.join(self.cifra.getDiretorio(), "Ativ. Individual 1 - Transp. Linha x Coluna - Texto Decifrado - " + self.cifra.getNomeArquivo()), "w")
        arquivoDecifrado.write(self.cifra.textoDecifrado)

    # Lê texto claro de arquivo
    def leTextoClaro(self):
        if len(self.cifra.caminho) == 0:
            raise ValueError("Escolha Um Arquivo Com Texto Claro!")

        arquivo = io.open(self.cifra.caminho, "rt", encoding="utf-8")
        texto = arquivo.read()

        if len(texto.strip()) == 0:
            raise ValueError("O Arquivo Está Vazio!")

        self.cifra.textoClaro = texto
        arquivo.close()

    # Configura os pares de chave e ordena de forma crescente em relação ao
    # caractere
    def setChave(self, chave):
		# Se a chave estiver vazia
        if len(chave.strip()) == 0:
            raise ValueError("Informe uma chave!")

		# Se a chave possuir mais de 7 caracteres
        if len(chave.strip()) > 7:
            raise ValueError("A Chave Pode Ter No Máximo 7 Caracteres!")

		# Limpa chave se possuir
        self.cifra.chave.clear()

		# Remove espaços no início e final da chave informada
        chave = chave.strip()

		# Para letra da chave
        for i in range(0, len(chave)):
			# Crio uma tupla com primeiro item igual à letra e segundo item igual à posição dessa letra na string
            par = tuple((chave[i], i))
			# Adiciona a tupla na chave
            self.cifra.chave.append(par)

		# Ordena itens
        self.cifra.sortChave()

	# Restaura objeto de cifra
    def reset(self):
        self.cifra = Cifra.Cifra()
