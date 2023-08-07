from CD import CD
from DVD import DVD
from CMidia import CMidia

class Programa:
    def main(self):
        produtos = [None] * 60

        print("Área de inserção de Dados:\n")
        cont = 0
        i = 0
        while i < 60:
            nome = input("Entre com o nome do produto:\n")
            codigo = int(input("Entre com o código do produto:\n"))
            preco = float(input("Entre com o preço do produto:\n"))
            resp = input("CD ou DVD?\n").lower()

            if resp == "cd":
                nmusicas = int(input("Entre com a quantidade de músicas do CD:\n"))
                c = CD(nome, codigo, preco, nmusicas)
                c.setNumMusicas(nmusicas)
                produtos[i] = c
            elif resp == "dvd":
                nfaixas = int(input("Entre com a quantidade de faixas do DVD:\n"))
                d = DVD(nome, codigo, preco, nfaixas)
                d.setNumFaixas(nfaixas)
                produtos[i] = d
            else:
                print("Resposta não válida.")
                continue

            cont += 1
            i += 1

            if i == 60:
                print("Limite de produtos alcançado.")
                break

            opc = int(input("Deseja continuar cadastrando? Sim (1) Não (2):\n"))
            if opc == 2:
                break

        for i in range(cont):
            produtos[i].printDados()

# Exemplo de uso
program = Programa()
program.main()
