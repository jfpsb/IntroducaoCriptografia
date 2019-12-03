from tkinter import Toplevel, Label, Button
class MessageBox:
    def __init__(self, titulo, mensagem, exec_depois):
        self.exec_depois = exec_depois
        self.janela = Toplevel()
        self.janela.title(titulo)
        self.janela.resizable(0, 0)
        self.janela.pack_propagate(0)

        fonteLabel = ("Century Gothic", 14)
        fonteButton = ("Century Gothic", 16, "bold")

        Label(self.janela, text=mensagem, font=fonteLabel).grid(row=0, column=0)
        Button(self.janela, text="Ok", font=fonteButton, command=self.close).grid(row = 1, column = 0)

        self.janela.update_idletasks()
        tela_w = self.janela.winfo_screenwidth()
        tela_h = self.janela.winfo_screenheight()
        janela_w = self.janela.winfo_reqwidth()
        janela_h = self.janela.winfo_reqheight()

        x = int((tela_w / 2) - (janela_w / 2))
        y = int((tela_h / 2) - (janela_h / 2))

        self.janela.geometry("+{}+{}".format(x, y))

    def close(self):
        self.janela.destroy()
        if self.exec_depois != None:
            self.exec_depois()