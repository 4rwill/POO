from equipamento import Equipamento
from computador import Computador
from impressora import Impressora
from itemJaExisteError import ItemJaExisteError

class Inventario:
    
    def __init__(self):
       self.__equipamentos = []
        
    
    def adicionar_item(self,item: Equipamento):
        for i in self.__equipamentos:
            if item.get_codigo_patrimonio() == i.get_codigo_patrimonio():
                raise ItemJaExisteError("Item já existente")
        if isinstance(item,Equipamento):
            self.__equipamentos.append(item)
            
    def remover_item(self,codigo_patrimonio):
        for i in self.__equipamentos:
            
            if i.get_codigo_patrimonio() == codigo_patrimonio:
                self.__equipamentos.remove(i)
                return
        raise ValueError("Equipamento não encontrado no inventário.")
    
    def listar_itens(self):
        computadores = [item for item in self.__equipamentos if isinstance(item, Computador)]                 
        impressoras = [item for item in self.__equipamentos if isinstance(item, Impressora)]   
        quantidade_computador = 0
        quantidade_impressora = 0
        if computadores:
            print("\n>>> Computadores:\n")
            for computador in computadores:
                quantidade_computador += 1
                print(f"COMPUTADOR {quantidade_computador}:")
                computador.imprime()   
                
                           
        if impressoras:   
            print("\n>>> Impressoras:\n")
            for impressora in impressoras:
                quantidade_impressora += 1
                print(f"IMPRESSORA {quantidade_impressora}:")
                impressora.imprime()   
        
        print(f"Quantidade Computadores: {quantidade_computador} ")        
        print(f"Quantidade Impressoras: {quantidade_impressora} ")        
                
                           
    def buscar_item(self, codigo_patrimonio):
        for i in self.__equipamentos:
            if i.get_codigo_patrimonio() == codigo_patrimonio:
                return i
        return None        
            
    def listar_computadores(self):
        computadores = [item for item in self.__equipamentos if isinstance(item,Computador)]
        
        if computadores:
            print("\n>>> Computadores:")
            for computador in computadores:
                computador.imprime()

                