from veiculo import Veiculo

from random import randint

class Caminhao(Veiculo):

    def __init__(self, fabricante, placa):
        super().__init__(fabricante, placa)
        self.__identificador = self.__criarIdentificador()
        self.__numeroRodas = 4
        self.__capacidadeCarga = 0


    def setFabricante(self, fabricante):
        return super().setFabricante(fabricante)
    
    def setPlaca(self, placa):
        return super().setPlaca(placa)

    def setNumeroRodas (self,rodas):
        if rodas < 4 or rodas > 20:
            raise ValueError("Número de rodas inválido")
        else:
            self.__numeroRodas = rodas

    def setCapacidadeCarga (self,carga):
        if carga < 0 or carga > 10:
            raise ValueError("Número de carga inválido")
        else:
            self.__capacidadeCarga = carga

    def getFabricante(self):
        return super().getFabricante()

    def getPlaca(self):
        return super().getPlaca()

    def getNumeroRodas(self):
        return self.__numeroRodas

    def getCapacidadeCarga(self):
        return self.__capacidadeCarga        
    
    def __criarIdentificador(self):
        identificador = randint(1,9999999)
        return identificador

    def imprime(self):
        super().imprime()
        print(f"Número de rodas: {self.__numeroRodas}")
        print(f"Capacidade carga: {self.__capacidadeCarga} Toneladas")
        print(f"Identificador: {self.__identificador}")

    