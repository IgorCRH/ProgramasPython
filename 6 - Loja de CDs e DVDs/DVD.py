from CMidia import CMidia

class DVD(CMidia):
    def __init__(self):
        super().__init__()
        self.nfaixas = 0
        
    def __init__(self, nome=None, codigo=None, preco=None, nfaixas=None, **kwargs):
        super().__init__(nome=nome, codigo=codigo, preco=preco)
        self.nfaixas = nfaixas

    def getTipo(self):
        return "\nDVD"

    def getInfo(self):
        return super().getInfo() + "\nQuantidade de Faixas: " + str(self.nfaixas)

    def setNumFaixas(self, nfaixas):
        self.nfaixas = nfaixas
