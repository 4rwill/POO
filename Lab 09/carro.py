from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, fabricante, numero_de_rodas, numero_de_portas, descricao):
        super().__init__(modelo, fabricante, numero_de_rodas, descricao)
        self.__numero_de_portas = numero_de_portas


    def getNumero_de_portas(self):
        return self.__numero_de_portas

    def setNumero_de_portas(self, numero_de_portas: int):
        self.__numero_de_portas = numero_de_portas

    def imprime(self):
        print("-----Modelo de Carro-----")
        super().imprime()
        print(f"Numero de Portas: {self.getNumero_de_portas()}\n")

    def emite_som(self):
        print("VRUMMMMM!!!\n")