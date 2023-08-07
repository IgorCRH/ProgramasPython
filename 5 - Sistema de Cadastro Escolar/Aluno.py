from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, email, data, cpf, matricula, cr):
        super().__init__(nome, email, data, cpf)
        self.matricula = matricula
        self.cr = cr

    def GetMatricula(self):
        return self.matricula

    def GetCR(self):
        return self.cr

    def novosaldo(self):
        if self.diarendimento != 0:
            diarendimento = float(input("Entre com o rendimento: "))
            self.saldo *= diarendimento
            print("O novo saldo é:", self.saldo)

    def cadaluno(self):
        self.nome = input("Entre com o nome do aluno: ")
        self.email = input("Entre com o email do aluno: ")
        self.data = input("Entre com a data de nascimento do aluno: ")
        self.cpf = input("Entre com o CPF do aluno: ")
        self.matricula = int(input("Entre com o número da matricula do aluno: "))
        self.cr = float(input("Entre com o CR do Aluno: "))

    def atualizaaluno(self, cpfatualizaaluno):
        if str(self.cpf) == cpfatualizaaluno:
            nomenov = input("Entre com o nome novo: ")
            emailnov = input("Entre com o email novo: ")
            cpfnov = int(input("Entre com o CPF novo: "))
            datanov = input("Entre com a data de nascimento nova: ")
            matnov = int(input("Entre com a matrícula nova: "))

            self.nome = nomenov
            self.email = emailnov
            self.cpf = cpfnov
            self.data = datanov
            self.matricula = matnov
        else:
            print("Aluno não encontrado.")
            
    def anulamatricula(self, cpfanulaaluno):
        if str(self.cpf) == cpfanulaaluno:
            self.matricula = 0
        else:
                print("Aluno não encontrado.")

    def listaralunos(self):
        print("Nome:", self.nome)
        print("E-mail:", self.email)
        print("CPF:", self.cpf)
        print("Data de Nascimento:", self.data)
        print("Matrícula:", self.matricula)
        print("CR:", self.cr)
