class ItemJaExisteError(Exception):

    def __init__(self, mensagem):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

    def __str__(self):
        return f'{self.mensagem}'