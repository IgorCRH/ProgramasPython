import tkinter as tk
from tkinter import ttk
from telavariavelqualitativa import TelaVariavelQualitativa
from teladistbinomial import TelaDistBinomial

class Telainicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Escolha qual cálculo deseja realizar")

        self.root.tk_setPalette("#070247")
        style = ttk.Style()
        style.theme_use('default')
        style.configure('Dark.TButton', foreground='white', background='#265699')

        self.tela_atual = None

        self.variavelqualitativa_button = ttk.Button(root, text="Calcular por Variavel Qualitativa", command=self.mostrar_tela_variavel_qualitativa, style='Dark.TButton')
        self.variavelqualitativa_button.pack(pady=10)

        self.distbinomial_button = ttk.Button(root, text="Calcular por Distribuição Binomial", command=self.mostrar_tela_dist_binomial, style='Dark.TButton')
        self.distbinomial_button.pack(pady=10)

    def mostrar_tela_variavel_qualitativa(self):
        if self.tela_atual:
            self.tela_atual.destroy()
        self.tela_atual = TelaVariavelQualitativa(self.root, self.mostrar_tela_principal)
        self.tela_atual.pack()

    def mostrar_tela_dist_binomial(self):
        if self.tela_atual:
            self.tela_atual.destroy()
        self.tela_atual = TelaDistBinomial(self.root, self.mostrar_tela_principal)
        self.tela_atual.pack()

    def mostrar_tela_principal(self):
        if self.tela_atual:
            self.tela_atual.destroy()
            self.tela_atual = None

if __name__ == "__main__":
    root = tk.Tk()
    app = Telainicial(root)
    root.mainloop()
