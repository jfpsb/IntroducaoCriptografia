from controller import Controller

class View:
    def __init__(self):
        # Instancia controller
        self.controller = Controller.Controller()

    # Inicia view
    def iniciar(self):
        print("Informe a chave: ")
        self.chave = input()
        print("Informe o caminho do texto claro: ")
        self.caminho = input()

        self.controller.setChave(self.chave)
        self.controller.cifra.caminho = self.caminho

        self.controller.leTextoClaro(self.caminho)

        self.controller.cifrar()
        self.controller.decifrar()
        
        self.controller.salvarCifrado()
        self.controller.salvarDecifrado()

        output = "Texto Cifrado e Decifrado Salvo em {}"
        print(output.format(self.controller.cifra.getDiretorio()))
