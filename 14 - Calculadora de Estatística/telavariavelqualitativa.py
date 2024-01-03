import tkinter as tk
from tkinter import ttk, messagebox

class TelaVariavelQualitativa(tk.Frame):
    def __init__(self, master, callback_vd):
        tk.Frame.__init__(self, master)
        self.master = master
        self.callback_vd = callback_vd

        self.master.title("Variável Qualitativa")
        style = ttk.Style()
        style.theme_use('default')
        style.configure('Dark.TButton', foreground='white', background='#265699')

        self.label_instrucao = tk.Label(self, text="Digite os valores e suas frequências separados por espaços:")
        self.label_instrucao.pack(pady=10)

        self.label_valores = tk.Label(self, text="Valores:")
        self.label_valores.pack()

        self.entry_valores = tk.Entry(self)
        self.entry_valores.pack()

        self.label_frequencias = tk.Label(self, text="Frequências:")
        self.label_frequencias.pack()

        self.entry_frequencias = tk.Entry(self)
        self.entry_frequencias.pack()

        self.button_calcular_vd = ttk.Button(self, text="Calcular Variância e Desvio Padrão", command=self.calcular_vd, style='Dark.TButton')
        self.button_calcular_vd.pack(pady=10)

        self.label_resultado = tk.Label(self, text="")
        self.label_resultado.pack()

    def calcular_vd(self):
        try:
            # Substitui vírgulas por pontos e depois faz a conversão para float
            valores = list(map(float, self.entry_valores.get().replace(',', ' ').split()))
            frequencias = list(map(float, self.entry_frequencias.get().split()))

            if len(valores) == 0 or len(valores) != len(frequencias):
                messagebox.showerror("Erro", "Número de valores e frequências deve ser igual e pelo menos um valor deve ser fornecido.")
                return

            media_ponderada = sum(v * f for v, f in zip(valores, frequencias)) / sum(frequencias)

            variancia = sum(f * ((v - media_ponderada) ** 2) for v, f in zip(valores, frequencias)) / sum(frequencias)
            desvio_padrao = variancia ** 0.5

            resultado = f"Variância: {variancia:.2f}\nDesvio Padrão: {desvio_padrao:.2f}"
            self.label_resultado.config(text=resultado)

            if self.callback_vd:
                self.callback_vd(variancia, desvio_padrao)

        except ValueError:
            messagebox.showerror("Erro", "Valores e frequências devem ser números.")
