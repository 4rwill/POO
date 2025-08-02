from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, fabricante, numero_de_rodas, cilindrada, descricao):
        super().__init__(modelo, fabricante, numero_de_rodas, descricao)
        self.__cilindrada = cilindrada


    def getCilindrada(self):
        return self.__cilindrada

    def setCilindrada(self, cilindrada: int):
        self.__cilindrada = cilindrada

    def imprime(self):
        print("-----Modelo de Moto-----")
        super().imprime()
        print(f"Cilindrada: {self.getCilindrada()}\n")

    def emite_som(self):
        print("TRA TRA TRA !!!\n")