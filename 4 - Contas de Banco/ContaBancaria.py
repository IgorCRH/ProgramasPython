class ContaBancaria:
    def __init__(self, cliente, numconta, saldo):
        self.cliente = cliente
        self.numconta = numconta
        self.saldo = saldo

    def getCliente(self):
        return self.cliente
    
    def getNumConta(self):
        return self.numconta
    
    def getSaldo(self):
        return self.saldo
