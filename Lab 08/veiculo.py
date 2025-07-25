class Veiculo: 
    def __init__(self, modelo, fabricante, numero_de_rodas, descricao):
        self.__modelo = modelo
        self.__fabricante = fabricante
        self.__numero_de_rodas = numero_de_rodas
        self.__descricao = descricao


    def getModelo(self):
        return self.__modelo

    def setModelo(self, modelo: str):
        self.__modelo = modelo

    def getFabricante(self):
        return self.__fabricante

    def setFabricante(self, fabricante: str):
        self.__fabricante = fabricante        
        
    def getNumero_de_rodas(self):
        return self.__numero_de_rodas

    def setNumero_de_rodas(self, numero_de_rodas: int):
        self.__numero_de_rodas = numero_de_rodas  

    def getDescricao(self):
        return self.__descricao

    def setDescricao(self, descricao: str):
        self.__descricao = descricao              


    def imprime(self):
        
            print(f"Modelo: {self.getModelo()}")
            print(f"Fabricante: {self.getFabricante()}")
            print(f"Número de Rodas: {self.getNumero_de_rodas()}")        
            print(f"Descrição: {self.getDescricao()}")

    def emite_som(self):
        pass         