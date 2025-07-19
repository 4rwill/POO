
from item import Item
from cd import CD
from dvd import DVD

class Catalogo:
   
    def __init__(self):
        self._itens = []

    def inserir_item(self, item: Item):
        self._itens.append(item)

    def remover_item(self, titulo: str):
        item_para_remover = self.pesquisar_item(titulo, retornar_objeto=True)
        if item_para_remover:
            self._itens.remove(item_para_remover)
        else:
            return False
        
    def pesquisar_item(self, titulo: str, retornar_objeto=False):
        for item in self._itens:
            if item.get_titulo().lower() == titulo.lower():
                if retornar_objeto:
                    return item
                else:
                    item.imprime()
                    return item
        if not retornar_objeto:
            return False
        return None

    def catalogo_vazio(self):
        return len(self._itens) == 0

    def listar_itens(self):
        if self.catalogo_vazio():
            print("O catálogo está vazio.")
            return

        print("\n=== LISTA COMPLETA DO CATÁLOGO ===")
        
        cds = [item for item in self._itens if isinstance(item, CD)]
        dvds = [item for item in self._itens if isinstance(item, DVD)]

        if cds:
            print("\n>>> CDs:")
            for cd in cds:
                cd.imprime()
        
        if dvds:
            print("\n>>> DVDs:")
            for dvd in dvds:
                dvd.imprime()