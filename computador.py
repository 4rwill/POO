from equipamento import Equipamento
class Computador(Equipamento):
    
    def __init__(self, codigo_patrimonio, fabricante, processador: str, memoria_ram: str):
        super().__init__(codigo_patrimonio, fabricante)
        self.__processador = processador
        self.__memoria_ram = memoria_ram
      
    def get_processador(self):
        return self.__processador
      
    def get_memoria_ram(self):
        return self.__memoria_ram
    
    def set_processador(self,processador: str):
        self.__processador = processador
        
    def set_memoria_ram(self,memoria_ram: str):
        self.__memoria_ram = memoria_ram
        
    
    def calcular_depreciacao(self):
        print("Depreciação de 15% ao ano para Computador.") 
      
      
        
    def imprime(self):
        
        super().imprime()   
        print(f"Processador: {self.__processador}")
        print(f"Memória Ram: {self.__memoria_ram}")
        print()
        
        
   