from item import Item

class DVD(Item):
   
    def __init__(self, titulo: str, tempo_reproducao: int, diretor: str, possuo: bool, comentario: str):
       
        super().__init__(titulo, tempo_reproducao, possuo, comentario)
        self.__diretor = diretor

    def imprime(self):
       
        print("--- Detalhes do DVD ---")
        super().imprime()
        print(f"Diretor: {self.get_diretor()}")

    def get_diretor(self):
        return self.__diretor

    def set_diretor(self, diretor: str):
        self.__diretor = diretor