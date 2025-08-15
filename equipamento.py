class Equipamento:
    
    def __init__(self, codigo_patrimonio:str, fabricante:str):
        self.__codigo_patrimonio = codigo_patrimonio
        self.__fabricante = fabricante
        self.__ativo = True
    
    def get_codigo_patrimonio(self):
        return self.__codigo_patrimonio  
    
    def get_fabricante(self):
        return self.__fabricante 
    
    def get_ativo(self):
        return self.__ativo
    
    def set_codigo_patrimonio(self, codigo_patrimonio: str):
        self.__codigo_patrimonio = codigo_patrimonio
        
    def set_fabricante(self, fabricante: str):
        self.__fabricante = fabricante
        
    def set_ativo(self, ativo: bool):
        self.__ativo = ativo
        
        
    def calcular_depreciacao(self):
       pass     
    
        
        
    def imprime(self):
        print(f"Código: {self.__codigo_patrimonio}")
        print(f"Fabricante: {self.__fabricante}")
        print(f"Ativo: {self.__ativo}")
        