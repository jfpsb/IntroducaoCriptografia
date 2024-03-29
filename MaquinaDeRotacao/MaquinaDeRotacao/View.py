import tkinter
from Controller import Controller
from tkinter import Label, Entry, filedialog, Toplevel, Button
from pathlib import Path
from MessageBox import MessageBox

class View:
    # Construtor
    def __init__(self):
        # Criando objeto de janela
        self.view = tkinter.Tk()
        self.view.title("Atividade Individual 2 - Criptografia por Máquina De Rotação")
        self.view.resizable(0, 1)
        self.view.pack_propagate(0)

        #Estilos de fonte
        self.fonteLabel = ("Century Gothic", 14)
        self.fonteButton = ("Century Gothic", 14, "bold")

        # Criando label
        self.lblArquivo = Label(self.view, text="Selecione o Arquivo Com o Texto Claro:", font=self.fonteLabel, wraplength=500)
        self.lblArquivo.grid(row = 0, column = 0)

        # Criando botões
        Button(self.view, text="Abrir Tela de Seleção", font=self.fonteButton, command=self.abrirFileDialog).grid(row = 0, column = 1)
        Button(self.view, text="Cifrar", font=self.fonteButton, command=self.cifrar).grid(row = 1, column = 0, columnspan = 2)

        # Configura posição da tela após inserir itens
        self.view.update_idletasks()
        tela_w = self.view.winfo_screenwidth()
        tela_h = self.view.winfo_screenheight()
        janela_w = self.view.winfo_reqwidth()
        janela_h = self.view.winfo_reqheight()
        self.view.geometry("+{}+{}".format(int(tela_w / 2 - janela_w / 2), int(tela_h / 2 - janela_h / 2)))
        self.view.columnconfigure(0, weight=1)

        # Instancia controller
        self.controller = Controller()

    # Inicia view
    def iniciar(self):
        self.view.mainloop()

    # Abre tela para escolher arquivo
    def abrirFileDialog(self):
        user_dir = str(Path.home())
        self.view.caminho = filedialog.askopenfilename(initialdir = user_dir,title = "Selecione O Texto",filetypes = [("Arquivos txt","*.txt")])
        if len(self.view.caminho) != 0:
            self.lblArquivo["text"] = self.view.caminho
            self.controller.cifra.caminho = self.view.caminho

    # Função executada ao apertar botão de cifrar
    def cifrar(self):
        try:
            self.controller.leTextoClaro()

            self.controller.cifrar()
            self.controller.decifrar()

            self.controller.salvarCifrado()
            self.controller.salvarDecifrado()

            messageBox = MessageBox("Cifragem Executada com Sucesso", "Texto Cifrado e Decifrado Salvo em {}".format(self.controller.cifra.getDiretorio()), self.reset)
        except ValueError as ve:
            messageBox = MessageBox("Erro ao Executar Cifragem", ve.args[0], None)
            print(ve.args)
        except FileNotFoundError as fnfe:
            messageBox = MessageBox("Erro ao Executar Cifragem", "Arquivo Não Encontrado", None)
            print(fnfe.args)

    # Reseta os campos da view e o modelo no controle
    def reset(self):
        self.lblArquivo["text"] = "Selecione o Arquivo Com o Texto Claro:"
        self.controller.reset()
