from Aluno import Aluno
from Funcionario import Funcionario

class Programa:
    def main(self):
        matricula = 0
        matnov = 0
        cpf = 0
        cpfnov = 0
        valor = 0
        opc = 0
        cr = 0
        salario = 0
        nome = " "
        nomenov = ""
        nanul = ""
        natt = ""
        email = " "
        emailnov = ""
        data = " "
        datanov = ""
        cargo = ""
        dep = ""

        a = Aluno(nome, email, data, cpf, matricula, cr)
        f = Funcionario(nome, email, data, cpf, salario, cargo, dep)

        while opc != 9:
            print("Digite a opção desejada:\n")
            print("1 - Cadastrar Aluno:\n")
            print("2 - Cadastrar Funcionário:\n")
            print("3 - Atualizar Dados do Aluno:\n")
            print("4 - Atualizar Dados do Funcionário:\n")
            print("5 - Reajustar Salário do Funcionário:\n")
            print("6 - Listar Alunos:\n")
            print("7 - Listar Funcionários:\n")
            print("8 - Anular Matrícula de Aluno:\n")
            opc = int(input())

            if opc == 1:
                a.cadaluno()
            elif opc == 2:
                f.cadfunc()
            elif opc == 3:
                print("Entre com o CPF do aluno que deseja atualizar:")
                cpfatualizaaluno = input()
                a.atualizaaluno(cpfatualizaaluno)
            elif opc == 4:
                print("Entre com o CPF do funcionário que deseja atualizar:")
                cpfatualizafunc = input()
                f.atualizafunc(cpfatualizafunc)
            elif opc == 5:
                print("Informe a quantia do reajuste:")
                valor = int(input())
                f.reajuste(valor)
            elif opc == 6:
                print("Lista dos Alunos:")
                a.listaralunos()
            elif opc == 7:
                print("Lista dos Funcionários:")
                f.listarfunc()
            elif opc == 8:
                print("Qual o nome do aluno que deseja anular matrícula?:")
                cpfanulaaluno = input()
                a.anulamatricula(cpfanulaaluno)

programa = Programa()
programa.main()
