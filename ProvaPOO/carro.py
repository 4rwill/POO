from veiculo import Veiculo
from random import randint

class Carro(Veiculo):

    def __init__(self, fabricante, placa, consumo: int):
        super().__init__(fabricante, placa)
        self.__nivelCombustivel = 0
        self.__portas = 4
        if consumo < 0: 
            raise ValueError("Consumo Inválido")
        else:
            self.__consumo = consumo

    def setFabricante(self, fabricante):
        return super().setFabricante(fabricante)
    
    def setPlaca(self, placa):
        return super().setPlaca(placa)
    
    def setConsumo(self,consumo):
        if consumo < 0:
            raise ValueError("Consumo inválido")  
        else:
            self.__consumo = consumo   

    def setPortas (self,portas):
        if portas < 1 or portas > 5:
            raise ValueError("Número de portas inválido")
        else:
            self.__portas = portas

    def setNivelCombustivel(self,nivelCombustivel):
        if nivelCombustivel < 1:
            raise ValueError("Nível de combustível inválido")  
        else:
            self.__nivelCombustivel = nivelCombustivel  
    
    def getFabricante(self):
        return super().getFabricante()

    def getPlaca(self):
        return super().getPlaca()
    
    def getConsumo(self):
        return self.__consumo
    
    def getPortas(self):
        return self.__portas
    
    def getNivelCombustivel(self):
        return self.__nivelCombustivel


    def mover(self, km:int):
        if km <= 0:
            raise ValueError("Insira um valor maior que 0")
        else:
            gasolinaGasta = km/self.__consumo
            if gasolinaGasta > self.__nivelCombustivel:
                raise ValueError ("Gasolina Insuficiente para trajeto")
            else:
                self.__nivelCombustivel -= gasolinaGasta

        super().mover(km)

    def gasolina(self):
        super().gasolina()
        return f"{self.getNivelCombustivel()} Litros"           

    def abastecer(self, litros):
         super().abastecer(litros)  
         if litros <= 0:
            raise ValueError("Insira valores maiores que 0")  
         else:
             self.__nivelCombustivel += litros         
    def imprime(self):
        super().imprime() 
        print(f"Consumo: {self.__consumo} KM/L")   
        print(f"Nível de Combustível: {self.__nivelCombustivel} Litros")
        print(f"Quantidade de Portas: {self.__portas} ")
   