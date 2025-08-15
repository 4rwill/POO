from equipamento import Equipamento

class Impressora(Equipamento):
    
    def __init__(self, codigo_patrimonio, fabricante, tipo_impressao: str):
        super().__init__(codigo_patrimonio, fabricante)
        self.__tipo_impressao = tipo_impressao
        
    def get_tipo_impressao(self):
        return self.__tipo_impressao
    
    def set_tipo_impressao(self, tipo_impressao: str):
        self.__tipo_impressao = tipo_impressao
        
    def imprime(self):
        super().imprime()    
        print(f"Tipo Impressão: {self.__tipo_impressao}")
        print()
    
    def calcular_depreciacao(self):
        print("Depreciação de 10% ao ano para Impressora.")    