from Controller import Controller
from Cifra import Cifra
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Separator
from pathlib import Path
from MessageBox import MessageBox

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
        fonteChave = ("Century Gothic", 10)
        self.fonteButton = ("Century Gothic", 14, "bold")

        # Frame
        frameDadosChave = tkinter.Frame(self.view)
        frameDadosChave.grid(
            row = 3,
            columnspan = 2,
            pady = (15, 0))

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
            font=self.fonteLabel,
            wraplength=500)

        self.lblChave = Label(
            self.view,
            text="Selecione o Arquivo Com A Chave Pública:",
            font=self.fonteLabel,
            wraplength=500)

        self.lblP.grid(
            row = 0,
            column = 0,
            ipady = 5)

        self.lblQ.grid(
            row = 1,
            column = 0,)

        self.lblArquivo.grid(
            row = 7,
            column = 0,
            columnspan = 2)

        self.lblChave.grid(
            row = 5,
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
            row = 4,
            column = 0,
            columnspan = 2,
            padx = 10,
            pady = 10,
            sticky="ew")

        Separator(self.view).grid(
            row = 9,
            column = 0,
            columnspan = 2,
            padx = 10,
            pady = 10,
            sticky="ew")

        # Criando botões
        Button(
            self.view,
            text="Gerar Chaves",
            font=self.fonteButton,
            command=self.gerarChaves).grid(
                row = 2,
                column = 0,
                columnspan = 2,
                sticky="ew",
                padx = 15,
                pady = (15, 0))

        Button(
            self.view,
            text="Abrir Tela de Seleção Para Texto Claro",
            font=self.fonteButton,
            command=self.abrirFileDialogTextoClaro).grid(
                row = 8,
                column = 0,
                columnspan = 2,
                sticky="ew",
                padx = 15)

        Button(
            self.view,
            text="Abrir Tela de Seleção Para Chave",
            font=self.fonteButton,
            command=self.abrirFileDialogChavePublica).grid(
                row = 6,
                column = 0,
                columnspan = 2,
                sticky="ew",
                padx = 15)

        Button(
            self.view,
            text="Cifrar",
            font=self.fonteButton,
            command=self.cifrar).grid(
                row = 10,
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
        self.controller = Controller(self)

    # Inicia view
    def iniciar(self):
        self.view.mainloop()

    # Abre tela para escolher arquivo com texto claro
    def abrirFileDialogTextoClaro(self):
        user_dir = str(Path.home())
        self.view.caminhoTextoClaro = filedialog.askopenfilename(initialdir = user_dir,title = "Selecione O Texto",filetypes = [("Arquivos txt","*.txt")])
        if len(self.view.caminhoTextoClaro) != 0:
            self.lblArquivo["text"] = self.view.caminhoTextoClaro
            self.controller.cifra.caminho = self.view.caminhoTextoClaro

    # Abre tela para escolher arquivo com chave pública
    def abrirFileDialogChavePublica(self):
        user_dir = str(Path.home())
        self.view.caminhoChavePublica = filedialog.askopenfilename(initialdir = user_dir,title = "Selecione A Chave Pública",filetypes = [("Arquivos txt","*.txt")])
        if len(self.view.caminhoChavePublica) != 0:
            self.lblChave["text"] = self.view.caminhoChavePublica
            self.controller.cifra.caminhoChavePublica = self.view.caminhoChavePublica

    # Chama função que gera as chaves públicas e privadas
    def gerarChaves(self):
        p = self.txtP.get()
        q = self.txtQ.get()

        try:
            result = self.controller.gerarChaves(p, q)
            if result == True:
                messageBox = MessageBox("Chaves Geradas Com Sucesso", "Chave Pública Salva Em " + str(Path.home()), None)
        except ValueError as ve:
            messageBox = MessageBox("Erro ao Executar Cifragem", ve.args[0], None)
            print(ve.args)

    # Função executada ao apertar botão de cifrar
    def cifrar(self):
        try:
            self.controller.carregarTextoClaro()
            self.controller.carregarChaves()

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
        self.lblChave["text"] = "Selecione o Arquivo Com A Chave Pública:"
        self.txtP.delete(0, "end")
        self.txtQ.delete(0, "end")
        self.controller.reset()
