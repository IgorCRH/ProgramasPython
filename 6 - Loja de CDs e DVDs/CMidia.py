from Midia import Midia

class CMidia(Midia):
    def __init__(self, nome, codigo, preco):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco

    def setNome(self, nome):
        self.nome = nome

    def setCodigo(self, codigo):
        self.codigo = codigo

    def setPreco(self, preco):
        self.preco = preco

    def getNome(self):
        return self.nome

    def getCodigo(self):
        return self.codigo

    def getPreco(self):
        return self.preco

    def getTipo(self):
        return "Tipo de Midia:\n"

    def getInfo(self):
        return f"Nome:\n{self.getNome()}\nCodigo:\n{self.getCodigo()}\nPreco:\n{self.getPreco()}"

    def printDados(self):
        print("Os detalhes do produto desta classe:\n")
        print(self.getInfo() + self.getTipo())

    def __init__(self):
        self.nome = "N/A"
        self.codigo = 0
        self.preco = 0
