class Item:
    
    def __init__(self, titulo: str, tempo_reproducao: int, possuo: bool, comentario: str):
      
        self._titulo = titulo
        self._tempo_reproducao = tempo_reproducao
        self._possuo = possuo
        self._comentario = comentario

    def get_titulo(self):
        return self._titulo

    def get_tempo_reproducao(self):
        return self._tempo_reproducao

    def get_possuo(self):
        return self._possuo

    def get_comentario(self):
        return self._comentario

    def set_titulo(self, titulo: str):
        self._titulo = titulo

    def set_tempo_reproducao(self, tempo_reproducao: int):
        self._tempo_reproducao = tempo_reproducao

    def set_possuo(self, possuo: bool):
        self._possuo = possuo

    def set_comentario(self, comentario: str):
        self._comentario = comentario

    def imprime(self):
     
        print(f"Título: {self.get_titulo()}")
        print(f"Tempo de Reprodução: {self.get_tempo_reproducao()} Minutos")
        print(f"Possuo: {'Sim' if self.get_possuo() else 'Não'}")
        print(f"Comentário: {self.get_comentario()}")