from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, cliente, numconta, saldo, diarendimento):
        super().__init__(cliente, numconta, saldo)
        self.diarendimento = diarendimento

    def GetDiaRendimento(self):
        return self.diarendimento

    def novosaldo(self):
        if self.diarendimento != 0:
            diarendimento = float(input("Entre com o rendimento: "))
            self.saldo *= diarendimento
            print("O novo saldo é:", self.saldo)

    def cadconta(self):
        self.cliente = input("Entre com o nome do cliente: ")
        self.numconta = int(input("Entre com o número da conta do cliente: "))
        self.saldo = float(input("Entre com o saldo da conta do cliente: "))
        self.diarendimento = float(input("Entre com o rendimento: "))

    def pesquisa(self):
        pesq = int(input("Entre com o número da conta que deseja listar: "))
        if pesq == self.numconta:
            print("Dados do Cliente:\n")
            print("Nome:", self.cliente)
            print("Número da Conta:", self.numconta)
            print("Saldo:", self.saldo)
        else:
            print("Não encontrado.")

    def exibir(self):
        print("Nome:", self.cliente)
        print("Número da Conta:", self.numconta)
        print("Saldo:", self.saldo)

    def sacar(self, quantia):
        numsaque = int(input("Entre com o número da conta no qual deseja sacar: "))
        if self.saldo > quantia and self.numconta == numsaque:
            self.saldo -= quantia
        elif self.saldo < quantia and self.saldo <= 0 and self.numconta == numsaque:
            print("O saldo está negativo, ou esta operação o deixará negativo.")

    def depositar(self, quantia):
        numdep = int(input("Entre com o número da conta no qual deseja depositar: "))
        if self.numconta == numdep:
            self.saldo += quantia
