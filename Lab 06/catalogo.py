from cd import CD

class Catalogo:
    def __init__(self):
        self.__cds = []

    def inserir_cd(self, cd: CD):

        self.__cds.append(cd)

    def remover_cd(self, cd: CD):

        self.__cds.remove(cd)

    def listar_cds(self):
       if len(self.__cds) == 0:
           return False
       
       for cd in self.__cds:
            cd.imprime()        

    def verificar_cd(self,titulo):

        for cd in self.__cds:
            if cd.get_titulo()== titulo:
                return cd.imprime()
            else:
                return False
    def tem_cds(self):
        if len(self.__cds) == 0:
            return False
        else:
            return True     

                
    def verificar_possuo_cd(self, titulo: str) -> bool:
        for cd in self.__cds:
            if cd.get_titulo() == titulo:
                return cd.get_possuo() 
                
        return False
    

    def listar_cds_que_possuo(self):
        

        
        cds_possuidos = [cd for cd in self.__cds if cd.get_possuo()]
        
        if not cds_possuidos:
            return False

        for cd in cds_possuidos:
            cd.imprime()

                       