class Pessoa:
    def __init__(self, nome, email, data, cpf):
        self.nome = nome
        self.email = email
        self.data = data
        self.cpf = cpf

    def getNome(self):
        return self.nome
    
    def getEmail(self):
        return self.email
    
    def getCpf(self):
        return self.cpf

    def getData(self):
        return self.data
