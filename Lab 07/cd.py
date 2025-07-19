from item import Item
import random
class CD(Item):
    def __init__(self, titulo: str, tempo_de_reproducao: int, artista: str, possuo: bool, comentario: str):
    
        super().__init__(titulo, tempo_de_reproducao, possuo, comentario)
        self.__artista = artista
        self.__numero_de_trilhas = self.__gerar_numero_de_trilhas()

    def imprime(self):
        
        print("--- Detalhes do CD ---")
        super().imprime()
        print(f"Artista: {self.get_artista()}")
        print(f"Número de Trilhas: {self.get_numero_de_trilhas()}")

    def __gerar_numero_de_trilhas(self):
        return random.randint(3,30)
    
    def get_artista(self):
        return self.__artista

    def set_artista(self, artista: str):
        self.__artista = artista

    def get_numero_de_trilhas(self):
        return self.__numero_de_trilhas

    def set_numero_de_trilhas(self, numero_de_trilhas: int):
        self.__numero_de_trilhas = numero_de_trilhas