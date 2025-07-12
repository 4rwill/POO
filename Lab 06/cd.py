import random
class CD:
    def __init__(self,titulo: int,tempo_de_reproducao: float,artista: str,possuo: bool,comentario: str):
         self.__titulo = titulo
         self.__tempo_de_reproducao = tempo_de_reproducao
         self.__artista = artista
         self.__numero_de_trilhas = self.__gerar_numero_de_trilhas()
         self.__possuo = possuo
         self.__comentario = comentario
        

    def imprime(self):
        print(f"Titulo:{self.__titulo} \n"
            f"Tempo de Reprodução: {self.__tempo_de_reproducao} Minutos \n"
            f"Artista: {self.__artista} \n"
            f"Numero de trilhas: {self.__numero_de_trilhas} \n"
            f"Possuo: {self.__possuo}\n"
            f"Comentário: {self.__comentario} \n"
            f"")

    def __gerar_numero_de_trilhas(self):
        return random.randint(3,30)
        
    def get_titulo(self) :
        return self.__titulo   
    
    def set_titulo(self, titulo:str):
        self.__titulo = titulo
        
    def get_tempo_de_reproducao(self) :
        return self.__tempo_de_reproducao   
    
    def set_tempo_de_reproducao(self, tempo_de_reproducao: float):
        self.__tempo_de_reproducao = tempo_de_reproducao

    def get_artista(self) :
        return self.__artista   
    
    def set_artista(self, artista:str):
        self.__artista = artista

    def get_numero_de_trilhas(self) :
        return self.__numero_de_trilhas   
    
    def set_numero_de_trilhas(self, numero_de_trilhas: int):
        self.__numero_de_trilhas = numero_de_trilhas  

    def get_possuo(self) :
        return self.__possuo   
    
    def set_possuo(self, possuo: bool):
        self.__possuo = possuo      

    def get_comentario(self) :
        return self.__comentario   
    
    def set_comentario(self, comentario: str):
        self.__comentario = comentario

    