from ContaBancaria import ContaBancaria

class ContaEspecial(ContaBancaria):
    def __init__(self, cliente, numconta, saldo, limite):
        super().__init__(cliente, numconta, saldo)
        self.limite = limite

    def GetLimite(self):
        return self.limite

    def cadconta(self):
        self.cliente = input("Entre com o nome do cliente: ")
        self.numconta = int(input("Entre com o número da conta do cliente: "))
        self.saldo = float(input("Entre com o saldo da conta do cliente: "))
        self.limite = float(input("Entre com o limite: "))

    def pesquisa(self):
        pesq = int(input("Entre com o número da conta que deseja listar: "))
        if pesq == self.numconta:
            print("Dados do Cliente:\n")
            print("Nome:", self.cliente)
            print("Número da Conta:", self.numconta)
            print("Saldo:", self.saldo)
            print("Limite:", self.limite)
        else:
            print("Não encontrado.")

    def exibir(self):
        print("Nome:", self.cliente)
        print("Número da Conta:", self.numconta)
        print("Saldo:", self.saldo)
        print("Limite:", self.limite)
        
    def sacaresp(self, quantia):
        numsaque = int(input("Entre com o número da conta no qual deseja sacar: "))
        if self.saldo < self.limite and quantia < self.limite and self.saldo > 0 and self.numconta == numsaque:
            self.saldo -= quantia
        else:
            print("Não é possível realizar a operação. Limite alcançado ou a conta não foi encontrada.")
    
    def depositar(self, quantia):
        numdep = int(input("Entre com o número da conta no qual deseja depositar: "))
        if self.numconta == numdep:
            self.saldo += quantia
