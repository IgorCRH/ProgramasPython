from CMidia import CMidia

class CD(CMidia):
    def __init__(self):
        super().__init__()
        self.nmusicas = 0
        
    def __init__(self, nome=None, codigo=None, preco=None, nmusicas=None, **kwargs):
        super().__init__(nome=nome, codigo=codigo, preco=preco)
        self.nmusicas = nmusicas

    def getTipo(self):
        return "\nCD"

    def getInfo(self):
        return super().getInfo() + "\nQuantidade de Músicas: " + str(self.nmusicas)

    def setNumMusicas(self, nmusicas):
        self.nmusicas = nmusicas
