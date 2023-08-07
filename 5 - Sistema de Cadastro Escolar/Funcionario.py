from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, email, data, cpf, salario, cargo, dep):
        super().__init__(nome, email, data, cpf)
        self.salario = salario
        self.cargo = cargo
        self.dep = dep

    def getSalario(self):
        return self.salario

    def getCargo(self):
        return self.cargo

    def getDep(self):
        return self.dep

    def cadfunc(self):
        self.nome = input("Entre com o nome do funcionário: ")
        self.email = input("Entre com o email do funcionário: ")
        self.data = input("Entre com a data de nascimento do funcionário: ")
        self.cpf = input("Entre com o CPF do funcionário: ")
        self.salario = float(input("Entre com o salário do funcionário: "))
        self.cargo = input("Entre com o cargo do funcionário: ")
        self.dep = input("Entre com o departamento do funcionário: ")

    def atualizafunc(self, cpfatualizafunc):
        if str(self.cpf) == cpfatualizafunc:
            nomenov = input("Entre com o nome novo: ")
            emailnov = input("Entre com o email novo: ")
            cpfnov = int(input("Entre com o CPF novo: "))
            datanov = input("Entre com a data de nascimento nova: ")
            cargonov = input("Entre com o cargo novo: ")

            self.nome = nomenov
            self.email = emailnov
            self.cpf = cpfnov
            self.data = datanov
            self.cargo = cargonov
        else:
            print("Funcionário não encontrado.")

    def listarfunc(self):
        print("Nome:", self.nome)
        print("E-mail:", self.email)
        print("CPF:", self.cpf)
        print("Data de Nascimento:", self.data)
        print("Cargo:", self.cargo)
        print("Departamento:", self.dep)
        print("Salário:", self.salario)

    def reajuste(self, valor):
        cpfreajuste = input("Entre com o nome do funcionário a receber reajuste: ")
        if self.cpf == cpfreajuste:
            self.salario += valor
        else:
            print("Funcionário não encontrado.")
