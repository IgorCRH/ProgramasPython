from ContaEspecial import ContaEspecial
from ContaPoupanca import ContaPoupanca

class ContasPython:
    def main(self):
        cliente = ""
        numconta = 0
        saldo = 0
        diarendimento = 0
        limite = 0
        c = ContaPoupanca(cliente, numconta, saldo, diarendimento)
        e = ContaEspecial(cliente, numconta, saldo, limite)

        while True:
            print("Digite a opção desejada:\n")
            print("1 - Cadastrar Cliente:\n")
            print("2 - Realizar Saque:\n")
            print("3 - Realizar Depósito:\n")
            print("4 - Exibir Novo Saldo a partir do Rendimento:\n")
            print("5 - Pesquisar Cliente:\n")
            print("6 - Listar Clientes:\n")
            print("7 - Sair:\n")
            opc = int(input())

            if opc == 1:
                print("Deseja cadastrar conta poupança (1) ou especial (2)?:\n")
                escolhe = int(input())
                if escolhe == 1:
                    c.cadconta()
                elif escolhe == 2:
                    e.cadconta()
            elif opc == 2:
                print("Entre com a quantia:\n")
                quantia = float(input())
                print("Sua conta é: conta poupança (1) ou especial (2)?:\n")
                escolhe = int(input())
                if escolhe == 1:
                    c.sacar(quantia)
                elif escolhe == 2:
                    e.sacaresp(quantia)
            elif opc == 3:
                print("Entre com a quantia:\n")
                quantia = float(input())
                print("Sua conta é: conta poupança (1) ou especial (2)?:\n")
                escolhe = int(input())
                if escolhe == 1:
                    c.depositar(quantia)
                elif escolhe == 2:
                    e.depositar(quantia)
            elif opc == 4:
                c.novosaldo()
            elif opc == 5:
                print("Sua conta é: conta poupança (1) ou especial (2)?:\n")
                escolhe = int(input())
                if escolhe == 1:
                    c.pesquisa()
                elif escolhe == 2:
                    e.pesquisa()
            elif opc == 6:
                print("Listagem dos Clientes:\n")
                print("Contas Poupança:\n")
                c.exibir()
                print("Contas Especiais:\n")
                e.exibir()
            elif opc == 7:
                break
            else:
                break

contas_program = ContasPython()
contas_program.main()
