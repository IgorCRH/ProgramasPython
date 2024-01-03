import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TelaDistBinomial(tk.Frame):
    def __init__(self, master, switch_callback):
        super().__init__(master)
        self.master = master
        self.switch_callback = switch_callback

        tk.Label(self, text="Tela Distribuição Normal").pack(pady=10)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Dark.TButton', foreground='white', background='#265699')

        self.label_prob_sucesso = tk.Label(self, text="Probabilidade de Sucesso (P(X)):")
        self.label_prob_sucesso.pack()
        self.entry_prob_sucesso = tk.Entry(self)
        self.entry_prob_sucesso.pack()

        self.label_num_dados = tk.Label(self, text="Número de Dados (n):")
        self.label_num_dados.pack()
        self.entry_num_dados = tk.Entry(self)
        self.entry_num_dados.pack()

        self.label_num_sucessos = tk.Label(self, text="Número de Sucessos (x):")
        self.label_num_sucessos.pack()
        self.entry_num_sucessos = tk.Entry(self)
        self.entry_num_sucessos.pack()

        self.button_calcular = ttk.Button(self, text="Calcular", command=self.calcular, style='Dark.TButton')
        self.button_calcular.pack(pady=10)

        self.label_resultado = tk.Label(self, text="")
        self.label_resultado.pack()

        ttk.Button(self, text="Voltar", command=self.voltar, style='Dark.TButton').pack(pady=10)

    def voltar(self):
        self.switch_callback()

    def calcular(self):
        try:
            prob_sucesso = float(self.entry_prob_sucesso.get())
            num_dados = int(self.entry_num_dados.get())
            num_sucessos = int(self.entry_num_sucessos.get())

            prob_binomial = self.calcular_prob_binomial(prob_sucesso, num_dados, num_sucessos)
            prob_cumu_abaixo = self.calcular_prob_cumu_abaixo(prob_sucesso, num_dados, num_sucessos)
            prob_cumu_acima = self.calcular_prob_cumu_acima(prob_sucesso, num_dados, num_sucessos)
            variancia = self.calcular_variancia(prob_sucesso, num_dados)
            valor_esperado = self.calcular_valor_esperado(prob_sucesso, num_dados)

            resultado = f"Probabilidade Binomial P(X={num_sucessos}): {prob_binomial:.4f}\n" \
                        f"Probabilidade Cumulativa P(X<{num_sucessos}): {prob_cumu_abaixo:.4f}\n" \
                        f"Probabilidade Cumulativa P(X>{num_sucessos}): {prob_cumu_acima:.4f}\n" \
                        f"Probabilidade Cumulativa P(X<={num_sucessos}): {prob_cumu_abaixo + prob_binomial:.4f}\n" \
                        f"Probabilidade Cumulativa P(X>={num_sucessos}): {prob_cumu_acima + prob_binomial:.4f}\n" \
                        f"Variância: {variancia:.4f}\n" \
                        f"Valor Esperado: {valor_esperado:.4f}"

            self.label_resultado.config(text=resultado)

        except ValueError:
            messagebox.showerror("Erro", "Certifique-se de que todos os campos estão preenchidos corretamente.")

    def calcular_prob_binomial(self, prob_sucesso, num_dados, num_sucessos):
        return (self.combinacao(num_dados, num_sucessos) * (prob_sucesso ** num_sucessos) *
                ((1 - prob_sucesso) ** (num_dados - num_sucessos)))

    def calcular_prob_cumu_abaixo(self, prob_sucesso, num_dados, num_sucessos):
        prob_cumu = 0
        for i in range(num_sucessos + 1):
            prob_cumu += self.calcular_prob_binomial(prob_sucesso, num_dados, i)
        return prob_cumu

    def calcular_prob_cumu_acima(self, prob_sucesso, num_dados, num_sucessos):
        prob_cumu = 0
        for i in range(num_sucessos, num_dados + 1):
            prob_cumu += self.calcular_prob_binomial(prob_sucesso, num_dados, i)
        return prob_cumu

    def calcular_variancia(self, prob_sucesso, num_dados):
        return num_dados * prob_sucesso * (1 - prob_sucesso)

    def calcular_valor_esperado(self, prob_sucesso, num_dados):
        return num_dados * prob_sucesso

    @staticmethod
    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        return n * TelaDistBinomial.fatorial(n - 1)

    def combinacao(self, n, k):
        return self.fatorial(n) / (self.fatorial(k) * self.fatorial(n - k))


if __name__ == "__main__":
    root = tk.Tk()
    app = TelaDistBinomial(root, None)
    root.mainloop()
