class Veiculo:

    def __init__(self,fabricante: str, placa: str):
        self.__fabricante = fabricante
        self.__placa = placa



    def setFabricante (self, fabricante):
        self.__fabricante = fabricante

    def setPlaca(self,placa):
        self.__placa = placa

    def getFabricante(self):
        return self.__fabricante        

    def getPlaca(self):
        return self.__placa        

    def mover(self,km):
        pass

    def gasolina(self):
        pass

    def abastecer(self, litros):
        pass

    def imprime(self):
        print(f"Fabricante: {self.getFabricante()}")
        print(f"Placa: {self.getPlaca()}")

