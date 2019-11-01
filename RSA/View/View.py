from Controller.Controller import Controller
from Model.Cifra import Cifra
import tkinter
from tkinter import *
from tkinter.ttk import Separator
from pathlib import Path
from View import MessageBox

class View:
    # Construtor
    def __init__(self):
        # Criando objeto de janela
        self.view = tkinter.Tk()
        self.view.title("Criptografia RSA")
        self.view.resizable(1, 1)
        self.view.pack_propagate(0)

        #Estilos de fonte
        self.fonteLabel = ("Century Gothic", 14)
        fonteEntry = ("Century Gothic", 12)
        self.fonteButton = ("Century Gothic", 14, "bold")

        # Criando labels
        self.lblP = Label(
            self.view,
            text="Informe o Número Primo P:",
            font=self.fonteLabel)

        self.lblQ = Label(
            self.view,
            text="Informe o Número Primo Q:",
            font=self.fonteLabel)

        self.lblArquivo = Label(
            self.view,
            text="Selecione o Arquivo Com o Texto Claro:",
            font=self.fonteLabel, wraplength=500)

        self.lblP.grid(
            row = 0,
            column = 0)

        self.lblQ.grid(
            row = 1,
            column = 0)

        self.lblArquivo.grid(
            row = 4,
            column = 0,
            columnspan = 2)

        # Criando entrada de texto
        self.txtP = Entry(
            self.view,
            font=fonteEntry)

        self.txtQ = Entry(
            self.view,
            font=fonteEntry)

        self.txtP.grid(
            row = 0,
            column = 1,
            padx = 5)

        self.txtQ.grid(
            row = 1,
            column = 1,
            padx = 5)

        Separator(self.view).grid(
            row = 3,
            column = 0,
            columnspan = 2,
            padx = 10,
            pady = 10,
            sticky="ew")

        Separator(self.view).grid(
            row = 6,
            column = 0,
            columnspan = 2,
            padx = 10,
            pady = 10,
            sticky="ew")

        # Criando botões
        Button(
            self.view,
            text="Gerar Chaves",
            font=self.fonteButton).grid(
                row = 2,
                column = 0,
                columnspan = 2,
                sticky="ew",
                padx = 15,
                pady = (15, 0))

        Button(
            self.view,
            text="Abrir Tela de Seleção",
            font=self.fonteButton,
            command=self.abrirFileDialog).grid(
                row = 5,
                column = 0,
                columnspan = 2,
                sticky="ew",
                padx = 15)

        Button(
            self.view,
            text="Cifrar",
            font=self.fonteButton,
            command=self.cifrar).grid(
                row = 7,
                column = 0,
                columnspan = 2,
                sticky="ew",
                padx = 15,
                pady = (0, 15))

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

        cifra = Cifra()

        print(cifra.mdc(66, 6670))

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