from controller import Controller
import tkinter
from tkinter import Label, Entry, filedialog, Toplevel, Button
from pathlib import Path
from view import MessageBox

class View:
    # Construtor
    def __init__(self):
        # Criando objeto de janela
        self.view = tkinter.Tk(screenName = "View")
        self.view.title("Atividade Individual 1 - Criptografia por Transposição")
        self.view.resizable(0, 0)
        self.view.pack_propagate(0)
        # Tela com tamanho 600 x 120 e abrindo centralizada
        self.view.update_idletasks()
        tela_w = self.view.winfo_screenwidth()
        tela_h = self.view.winfo_screenheight()
        self.view.geometry("600x120+{}+{}".format(int(tela_w / 2 - 600 / 2), int(tela_h / 2 - 120 / 2)))
        self.view.columnconfigure(0, weight=1)

        #Estilos de fonte
        self.fonteLabel = ("Century Gothic", 14)
        fonteEntry = ("Century Gothic", 12)
        self.fonteButton = ("Century Gothic", 14, "bold")

        # Criando labels
        Label(self.view, text="Informe a Chave: ", font=self.fonteLabel).grid(row=0, column = 0)
        self.lblArquivo = Label(self.view, text="Selecione o Arquivo Com o Texto Claro:", font=self.fonteLabel, wraplength=500)
        self.lblArquivo.grid(row = 1, column = 0)

        # Criando elemento de entrada de texto
        self.txtChave = Entry(self.view, font=fonteEntry)
        self.txtChave.grid(row = 0, column = 1)

        # Criando botões
        Button(self.view, text="Abrir Tela de Seleção", font=self.fonteButton, command=self.abrirFileDialog).grid(row = 1, column = 1)
        Button(self.view, text="Cifrar", font=self.fonteButton, command=self.cifrar).grid(row = 2, column = 0, columnspan = 2)

        # Instancia controller
        self.controller = Controller.Controller()

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
        chave = self.txtChave.get()

        try:
            self.controller.leTextoClaro()
            self.controller.setChave(chave.strip())

            self.controller.cifrar()
            self.controller.decifrar()

            self.controller.salvarCifrado()
            self.controller.salvarDecifrado()

            messageBox = MessageBox.MessageBox("Cifragem Executada com Sucesso", "Texto Cifrado e Decifrado Salvo em {}".format(self.controller.cifra.getDiretorio()), self.reset)
        except ValueError as ve:
            messageBox = MessageBox.MessageBox("Erro ao Executar Cifragem", ve.args[0], None)
            print(ve.args)
        except FileNotFoundError as fnfe:
            messageBox = MessageBox.MessageBox("Erro ao Executar Cifragem", "Arquivo Não Encontrado", None)
            print(fnfe.args)

    # Reseta os campos da view e o modelo no controle
    def reset(self):
        self.lblArquivo["text"] = "Selecione o Arquivo Com o Texto Claro:"
        self.txtChave.delete(0, "end")
        self.controller.reset()
