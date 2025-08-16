from veiculo import Veiculo
from carro import Carro
from caminhao import Caminhao

class Frota:

    def __init__(self):
        self.__veiculos = []

    def inserirVeiculos(self,veiculo):
        if not isinstance(veiculo,Veiculo):
            raise ValueError("Não é um veículo")
        else:
            self.__veiculos.append(veiculo)    

    def removerVeiculos(self,veiculo):
        for i in self.__veiculos:
            if veiculo not in self.__veiculos:
                raise ValueError("Veículo não está na frota") 
            else:
                self.__veiculos.remove(veiculo)     

    def frotaVazia(self):
        if len(self.__veiculos) == 0:
            return True          
        else:
            return False  
        
    def listarVeiculos(self):

        carros = [i for i in self.__veiculos if isinstance(i,Carro)]
        caminhoes = [i for i in self.__veiculos if isinstance(i,Caminhao)]

        if carros:
            print("//CARROS:\n")
            for carro in carros:
                carro.imprime()
                print("-"*10)

        if caminhoes:
            print("//CAMINHÕES:\n")
            for caminhao in caminhoes:
                caminhao.imprime()
                print("-"*10)   

    
