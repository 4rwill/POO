
from veiculo import Veiculo
from bicicleta import Bicicleta
from carro import Carro
from moto import Moto


class Frota:
   
    def __init__(self):
        self.__veiculos = []

    def inserir_veiculo(self, veiculo: Veiculo):
        if isinstance(veiculo, Veiculo):
            self.__veiculos.append(veiculo)

    def remover_veiculo(self, veiculo: Veiculo):
        if isinstance(veiculo,Veiculo):
            self.__veiculos.remove(veiculo)
        else:
            return False
        
    def remover_moto(self, moto: Moto):
        if isinstance(moto,Moto):
            self.__veiculos.remove(moto)
        else:
            return False        


    def frota_vazia(self):
        return len(self.__veiculos) == 0
    
    def frota_sem_motos(self): 
        for veiculo in self.__veiculos: 
            if isinstance(veiculo, Moto):
                print("Tem Moto")
                return False
        print("Frota Sem Moto")
        return True  
    
    def buscar_carro_por_modelo(self, modelo: str):
        for veiculo in self.__veiculos:
            
            if isinstance(veiculo, Carro):
                
                if veiculo.getModelo().lower() == modelo.lower():
                    return veiculo.imprime() 
                    
        return None
            

    def listar_frota(self):
        if self.frota_vazia():
            print("A Frota está vazia.")
            return

        print("\n=== LISTA COMPLETA DA FROTA ===")
        
        carros = [veiculo for veiculo in self.__veiculos if isinstance(veiculo, Carro)]
        motos = [veiculo for veiculo in self.__veiculos if isinstance(veiculo, Moto)]
        bicicletas = [veiculo for veiculo in self.__veiculos if isinstance(veiculo, Bicicleta)]


        if carros:
            print("\n>>> Carros:")
            for carro in carros:
                carro.imprime()
        
        if motos:
            print("\n>>> Motos:")
            for moto in motos:
                moto.imprime()
                

        if bicicletas:
            print("\n>>> Bicicletas:")
            for bicicleta in bicicletas:
                bicicleta.imprime()



