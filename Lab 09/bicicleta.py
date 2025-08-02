from veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, modelo, fabricante, numero_de_rodas, numero_de_marchas, descricao):
        super().__init__(modelo, fabricante, numero_de_rodas, descricao)
        self.__numero_de_marchas = numero_de_marchas


    def getNumeroDeMarchas(self):
        return self.__numero_de_marchas

    def setCilindrada(self, numero_de_marchas: int):
        self.__numero_de_marchas = numero_de_marchas

    def imprime(self):
        print("-----Modelo de Bicicleta-----")
        super().imprime()
        print(f"Numero de Marchas: {self.getNumeroDeMarchas()}\n")

    def emite_som(self):
        print("BI BI !!!\n")